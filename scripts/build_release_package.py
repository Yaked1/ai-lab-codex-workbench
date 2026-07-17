#!/usr/bin/env python3
"""Build a commit-exact release ZIP and JSON manifest for this workbench."""
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

PACKAGE_NAME = "ai-agent-coding-workbench"
FIXED_ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
MAX_PACKAGE_FILE_BYTES = 5_000_000
TOP_LEVEL_FILES = (
    "README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", "SECURITY.md",
    "CODE_OF_CONDUCT.md", "SUPPORT.md", "CITATION.cff", "CHANGELOG.md", "LICENSE",
)
PACKAGE_DIRS = ("data", "docs", "prompts", "scripts", "tests", "skills", "examples", "starter")
PACKAGE_SUBDIRS = (PurePosixPath(".github/workflows"), PurePosixPath(".github/codex/prompts"))
REQUIRED_PACKAGE_PATHS = tuple(PurePosixPath(path) for path in TOP_LEVEL_FILES + PACKAGE_DIRS) + PACKAGE_SUBDIRS
EXCLUDED_DIR_NAMES = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache", ".cache", "dist", "build", "logs", "outputs", "secret", "secrets", "private"}
EXCLUDED_SUFFIXES = {".7z", ".bak", ".bin", ".ckpt", ".db", ".gguf", ".gz", ".h5", ".joblib", ".key", ".log", ".onnx", ".p12", ".pem", ".pickle", ".pkl", ".pth", ".pt", ".pyc", ".pyo", ".rar", ".safetensors", ".sqlite", ".tar", ".tgz", ".tmp", ".zip"}
VERSION_PATTERN = re.compile(r"v?\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?")


class BuildOutputs(NamedTuple):
    zip_path: Path
    manifest_path: Path


class PublishedOutput(NamedTuple):
    path: Path
    identity: tuple[int, int, int, int]


def validate_version(version: str) -> str:
    version = version.strip()
    if not VERSION_PATTERN.fullmatch(version) or ".." in version:
        raise ValueError("Version must look like vMAJOR.MINOR.PATCH, for example v0.1.0 or v0.2.0-beta.1.")
    return version


def _git(root: Path, *args: str) -> bytes:
    try:
        return subprocess.run(
            ["git", "-C", os.fspath(root), *args],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).stdout
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
        if not record:
            continue
        metadata, raw_path = record.split(b"\t", 1)
        mode, object_type, _object_id, raw_size = metadata.split()
        if object_type != b"blob":
            continue
        entries.append((mode.decode("ascii"), raw_path.decode("utf-8", "surrogateescape"), int(raw_size)))
    return entries


def _has_excluded_name(relative: PurePosixPath) -> bool:
    for part in relative.parts:
        lowered = part.lower()
        if lowered in EXCLUDED_DIR_NAMES or lowered == ".env" or lowered.startswith(".env."):
            return True
        if lowered.startswith(("secret.", "secret-", "private.", "private-")):
            return True
    return False


def _is_allowed(relative: PurePosixPath) -> bool:
    if relative.as_posix() in TOP_LEVEL_FILES:
        return True
    if relative.parts and relative.parts[0] in PACKAGE_DIRS:
        return True
    return any(relative == directory or directory in relative.parents for directory in PACKAGE_SUBDIRS)


def _validate_required_paths(paths: set[str]) -> None:
    missing = []
    for required in REQUIRED_PACKAGE_PATHS:
        name = required.as_posix()
        if name in TOP_LEVEL_FILES:
            present = name in paths
        else:
            present = any(path.startswith(f"{name}/") for path in paths)
        if not present:
            missing.append(name)
    if missing:
        raise FileNotFoundError(f"Missing required committed package path(s): {', '.join(missing)}")


def committed_package_paths(root: Path, commit: str) -> list[str]:
    candidates = _tree_entries(root, commit)
    _validate_required_paths({path for mode, path, _size in candidates if mode != "120000"})
    included = []
    for mode, path, size in candidates:
        relative = PurePosixPath(path)
        if mode == "120000" or not _is_allowed(relative) or _has_excluded_name(relative):
            continue
        if relative.suffix.lower() in EXCLUDED_SUFFIXES or size > MAX_PACKAGE_FILE_BYTES:
            continue
        included.append(path)
    return sorted(included)


def committed_blob(root: Path, commit: str, relative: str) -> bytes:
    return _git(root, "cat-file", "blob", f"{commit}:{relative}")


def iter_package_files(root: Path) -> list[Path]:
    commit = source_commit(root)
    return [root / Path(relative) for relative in committed_package_paths(root, commit)]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _write_zip(path: Path, blobs: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, data in blobs.items():
            info = zipfile.ZipInfo(relative, FIXED_ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, data)


def _manifest(version: str, zip_path: Path, commit: str, blobs: dict[str, bytes]) -> dict[str, object]:
    entries = []
    for relative, data in blobs.items():
        entries.append({"path": relative, "size_bytes": len(data), "sha256": sha256_bytes(data)})
    return {
        "package_name": PACKAGE_NAME,
        "version": version,
        "source_commit": commit,
        "archive": {"name": zip_path.name, "size_bytes": zip_path.stat().st_size, "sha256": sha256_file(zip_path)},
        "included_paths": [path.as_posix() for path in REQUIRED_PACKAGE_PATHS],
        "excluded_rules": {"directories": sorted(EXCLUDED_DIR_NAMES), "suffixes": sorted(EXCLUDED_SUFFIXES), "env_files": [".env", ".env.*"], "max_file_bytes": MAX_PACKAGE_FILE_BYTES},
        "files": entries,
    }


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


def build_package(version: str, root: Path, output_dir: Path | None = None) -> BuildOutputs:
    version = validate_version(version)
    root = root.resolve()
    commit = source_commit(root)
    files = committed_package_paths(root, commit)
    output_dir = (output_dir or root / "dist").resolve()
    zip_path = output_dir / f"{PACKAGE_NAME}-{version}.zip"
    manifest_path = output_dir / f"package-manifest-{version}.json"
    if zip_path.exists() or manifest_path.exists():
        raise FileExistsError(f"Refusing to overwrite existing package output for {version}.")

    output_dir.mkdir(parents=True, exist_ok=True)
    zip_temp: Path | None = None
    manifest_temp: Path | None = None
    published: list[PublishedOutput] = []
    try:
        zip_temp = _temp_path(output_dir, ".zip")
        manifest_temp = _temp_path(output_dir, ".json")
        blobs = {relative: committed_blob(root, commit, relative) for relative in files}
        _write_zip(zip_temp, blobs)
        manifest = _manifest(version, zip_temp, commit, blobs)
        manifest["archive"]["name"] = zip_path.name
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
    return BuildOutputs(zip_path=zip_path, manifest_path=manifest_path)


def display_path(path: Path) -> Path:
    try:
        return path.relative_to(Path.cwd())
    except ValueError:
        return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a commit-exact release zip package and manifest.")
    parser.add_argument("--version", required=True, help="Release version, for example v0.1.0")
    parser.add_argument("--root", default=Path(__file__).resolve().parents[1], type=Path)
    parser.add_argument("--output-dir", default=None, type=Path)
    args = parser.parse_args()
    try:
        outputs = build_package(args.version, args.root, args.output_dir)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"Built {display_path(outputs.zip_path)}")
    print(f"Wrote {display_path(outputs.manifest_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
