#!/usr/bin/env python3
"""Build a commit-exact deterministic Prompting OS ZIP and manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from typing import NamedTuple

PACKAGE_STEM = "prompting-os"
DEFAULT_VERSION = "v1"
PACKAGE_ROOT = "Prompting_OS_v1"
FIXED_ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
MAX_PACKAGE_FILE_BYTES = 5_000_000
VERSION_PATTERN = re.compile(r"v?\d+(?:\.\d+){0,2}(?:-[0-9A-Za-z.-]+)?")
EXCLUDED_DIR_NAMES = {".cache", ".git", ".mypy_cache", ".pytest_cache", ".venv", "__pycache__", "build", "dist", "logs", "node_modules", "outputs", "private", "secret", "secrets", "venv"}
EXCLUDED_SUFFIXES = {".7z", ".bak", ".bin", ".db", ".gguf", ".gz", ".key", ".log", ".p12", ".pem", ".pyc", ".pyo", ".rar", ".sqlite", ".tar", ".tgz", ".tmp", ".zip"}


class PackageOutputs(NamedTuple):
    zip_path: Path
    manifest_path: Path


class PublishedOutput(NamedTuple):
    path: Path
    identity: tuple[int, int, int, int]


def normalize_version(version: str) -> str:
    label = version.strip()
    if not VERSION_PATTERN.fullmatch(label) or ".." in label:
        raise ValueError("Version must look like v1, v1.2.0, or v1.2.0-beta.1.")
    return label if label.startswith("v") else f"v{label}"


def resolve_path(base: Path, path: Path | None, default: Path) -> Path:
    return default.resolve() if path is None else (path.resolve() if path.is_absolute() else (base / path).resolve())


def display_relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.name


def _git(root: Path, *args: str) -> bytes:
    try:
        return subprocess.run(["git", "-C", os.fspath(root), *args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError("Git repository with a committed HEAD is required for packaging.") from exc


def source_commit(root: Path) -> str:
    repository_root = Path(os.fsdecode(_git(root, "rev-parse", "--show-toplevel")).rstrip("\r\n")).resolve()
    if repository_root != root.resolve():
        raise ValueError("Packaging root must be the Git repository top level.")
    return _git(root, "rev-parse", "--verify", "HEAD^{commit}").decode("ascii").strip()


def _tree_entries(root: Path, commit: str) -> list[tuple[str, str, int]]:
    entries = []
    for record in _git(root, "ls-tree", "-rlz", "--full-tree", commit).split(b"\0"):
        if record:
            metadata, raw_path = record.split(b"\t", 1)
            mode, kind, _object_id, raw_size = metadata.split()
            if kind == b"blob":
                entries.append((mode.decode("ascii"), raw_path.decode("utf-8", "surrogateescape"), int(raw_size)))
    return entries


def _excluded(relative: PurePosixPath) -> bool:
    for part in relative.parts:
        lowered = part.lower()
        if lowered in EXCLUDED_DIR_NAMES or lowered == ".env" or lowered.startswith(".env."):
            return True
        if lowered.startswith(("secret.", "secret-", "private.", "private-")):
            return True
    return relative.suffix.lower() in EXCLUDED_SUFFIXES


def _prefix_paths(root: Path, commit: str, prefix: PurePosixPath) -> list[str]:
    prefix_text = prefix.as_posix()
    files = []
    for mode, path, size in _tree_entries(root, commit):
        relative = PurePosixPath(path)
        if mode == "120000":
            continue
        try:
            source_relative = relative.relative_to(prefix)
        except ValueError:
            continue
        if _excluded(source_relative) or size > MAX_PACKAGE_FILE_BYTES:
            continue
        files.append(path)
    if not files:
        raise FileNotFoundError(f"Missing committed source prefix: {prefix_text}")
    return sorted(files)


def committed_package_paths(root: Path, commit: str) -> list[str]:
    return _prefix_paths(root, commit, PurePosixPath("docs/prompting-os"))


def committed_blob(root: Path, commit: str, relative: str) -> bytes:
    return _git(root, "cat-file", "blob", f"{commit}:{relative}")


def has_excluded_name(relative: Path) -> bool:
    return _excluded(PurePosixPath(relative.as_posix()))


def should_include(path: Path, source_dir: Path) -> bool:
    return path.is_file() and not _excluded(PurePosixPath(path.relative_to(source_dir).as_posix())) and path.stat().st_size <= MAX_PACKAGE_FILE_BYTES


def iter_source_files(source_dir: Path) -> list[Path]:
    return sorted(path for path in source_dir.rglob("*") if should_include(path, source_dir))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _file_identity(path: Path) -> tuple[int, int, int, int]:
    stat = path.stat(follow_symlinks=False)
    return (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns)


def _remove_owned_output(output: PublishedOutput) -> None:
    try:
        current_identity = _file_identity(output.path)
    except FileNotFoundError:
        return
    if current_identity == output.identity:
        output.path.unlink()


def _publish_new(temp_path: Path, final_path: Path) -> tuple[int, int, int, int]:
    identity = _file_identity(temp_path)
    os.link(temp_path, final_path)
    try:
        if _file_identity(final_path) != identity:
            raise OSError(f"Published output identity changed unexpectedly: {final_path}")
    except Exception:
        _remove_owned_output(PublishedOutput(final_path, identity))
        raise
    return identity


def _temp_path(output_dir: Path, suffix: str) -> Path:
    descriptor, name = tempfile.mkstemp(prefix=".package-", suffix=suffix, dir=output_dir)
    os.close(descriptor)
    return Path(name)


def _cleanup_temps(paths: list[Path | None]) -> list[OSError]:
    errors = []
    for path in paths:
        if path is None:
            continue
        try:
            path.unlink(missing_ok=True)
        except OSError as exc:
            errors.append(exc)
    return errors


def _rollback_outputs(outputs: list[PublishedOutput]) -> list[OSError]:
    errors = []
    for output in reversed(outputs):
        try:
            _remove_owned_output(output)
        except OSError as exc:
            errors.append(exc)
    return errors


def build_package(root: Path, version: str = DEFAULT_VERSION, source_dir: Path | None = None, output_dir: Path | None = None) -> PackageOutputs:
    root = root.resolve()
    version = normalize_version(version)
    source_dir = resolve_path(root, source_dir, root / "docs" / "prompting-os")
    try:
        prefix = PurePosixPath(source_dir.relative_to(root).as_posix())
    except ValueError as exc:
        raise ValueError("source_dir must be inside the repository root") from exc
    commit = source_commit(root)
    files = _prefix_paths(root, commit, prefix)
    output_dir = resolve_path(root, output_dir, root / "release" / "packages")
    zip_path = output_dir / f"{PACKAGE_STEM}-{version}.zip"
    manifest_path = output_dir / f"{PACKAGE_STEM}-{version}-manifest.json"
    if zip_path.exists() or manifest_path.exists():
        raise FileExistsError(f"Refusing to overwrite existing package output for {version}.")
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_temp: Path | None = None
    manifest_temp: Path | None = None
    published: list[PublishedOutput] = []
    try:
        zip_temp = _temp_path(output_dir, ".zip")
        manifest_temp = _temp_path(output_dir, ".json")
        entries = []
        with zipfile.ZipFile(zip_temp, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for relative in files:
                archive_relative = PurePosixPath(relative).relative_to(prefix).as_posix()
                archive_path = f"{PACKAGE_ROOT}/{archive_relative}"
                data = committed_blob(root, commit, relative)
                info = zipfile.ZipInfo(archive_path, FIXED_ZIP_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                archive.writestr(info, data)
                entries.append({"path": relative, "archive_path": archive_path, "size_bytes": len(data), "sha256": sha256_bytes(data)})
        manifest = {"package_name": PACKAGE_STEM, "version": version, "source_commit": commit, "source_dir": prefix.as_posix(), "package_root": PACKAGE_ROOT, "archive": {"name": zip_path.name, "size_bytes": zip_temp.stat().st_size, "sha256": sha256_file(zip_temp)}, "excluded_rules": {"directories": sorted(EXCLUDED_DIR_NAMES), "suffixes": sorted(EXCLUDED_SUFFIXES), "env_files": [".env", ".env.*"], "max_file_bytes": MAX_PACKAGE_FILE_BYTES}, "files": entries}
        manifest_temp.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        published.append(PublishedOutput(zip_path, _publish_new(zip_temp, zip_path)))
        published.append(PublishedOutput(manifest_path, _publish_new(manifest_temp, manifest_path)))
    except Exception as exc:
        cleanup_errors = _rollback_outputs(published) + _cleanup_temps([zip_temp, manifest_temp])
        if cleanup_errors and hasattr(exc, "add_note"):
            exc.add_note("Package cleanup also failed: " + "; ".join(str(error) for error in cleanup_errors))
        raise
    cleanup_errors = _cleanup_temps([zip_temp, manifest_temp])
    if cleanup_errors:
        rollback_errors = _rollback_outputs(published)
        retry_errors = _cleanup_temps([zip_temp, manifest_temp])
        details = cleanup_errors + rollback_errors + retry_errors
        raise OSError("Package publication cleanup failed: " + "; ".join(str(error) for error in details))
    return PackageOutputs(zip_path=zip_path, manifest_path=manifest_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a commit-exact Prompting OS release ZIP and manifest.")
    parser.add_argument("--root", default=Path(__file__).resolve().parents[1], type=Path)
    parser.add_argument("--version", default=DEFAULT_VERSION)
    parser.add_argument("--source-dir", default=None, type=Path)
    parser.add_argument("--output-dir", default=None, type=Path)
    args = parser.parse_args()
    try:
        outputs = build_package(args.root, args.version, args.source_dir, args.output_dir)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"Built {display_relative(outputs.zip_path, args.root)}")
    print(f"Wrote {display_relative(outputs.manifest_path, args.root)}")
    print(f"SHA256 {sha256_file(outputs.zip_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
