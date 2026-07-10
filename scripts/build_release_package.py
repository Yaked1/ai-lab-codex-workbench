#!/usr/bin/env python3
"""Build the release ZIP and JSON manifest for this workbench."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from typing import NamedTuple

PACKAGE_NAME = "ai-agent-coding-workbench"
FIXED_ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
MAX_PACKAGE_FILE_BYTES = 5_000_000

TOP_LEVEL_FILES = (
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    "LICENSE",
)

PACKAGE_DIRS = (
    "data",
    "docs",
    "prompts",
    "scripts",
    "tests",
)

PACKAGE_SUBDIRS = (
    Path(".github") / "workflows",
    Path(".github") / "codex" / "prompts",
)

REQUIRED_PACKAGE_PATHS = tuple(Path(path) for path in TOP_LEVEL_FILES) + tuple(
    Path(path) for path in PACKAGE_DIRS
) + PACKAGE_SUBDIRS

EXCLUDED_DIR_NAMES = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".cache",
    "dist",
    "build",
    "logs",
    "outputs",
    "secret",
    "secrets",
    "private",
}

EXCLUDED_SUFFIXES = {
    ".7z",
    ".bak",
    ".bin",
    ".ckpt",
    ".db",
    ".gguf",
    ".gz",
    ".h5",
    ".joblib",
    ".key",
    ".log",
    ".onnx",
    ".p12",
    ".pem",
    ".pickle",
    ".pkl",
    ".pth",
    ".pt",
    ".pyc",
    ".pyo",
    ".rar",
    ".safetensors",
    ".sqlite",
    ".tar",
    ".tgz",
    ".tmp",
    ".zip",
}

VERSION_PATTERN = re.compile(r"v?\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?")


class BuildOutputs(NamedTuple):
    zip_path: Path
    manifest_path: Path


def validate_version(version: str) -> str:
    version = version.strip()
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError(
            "Version must look like vMAJOR.MINOR.PATCH, for example v0.1.0 "
            "or v0.2.0-beta.1."
        )
    if ".." in version:
        raise ValueError("Version must not contain consecutive dots.")
    return version


def validate_required_paths(root: Path) -> None:
    missing = [path.as_posix() for path in REQUIRED_PACKAGE_PATHS if not (root / path).exists()]
    if missing:
        joined = ", ".join(missing)
        raise FileNotFoundError(f"Missing required package path(s): {joined}")


def is_under_path(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def is_allowed_package_path(relative: Path) -> bool:
    if relative.as_posix() in TOP_LEVEL_FILES:
        return True
    if relative.parts and relative.parts[0] in PACKAGE_DIRS:
        return True
    return any(is_under_path(relative, package_subdir) for package_subdir in PACKAGE_SUBDIRS)


def has_excluded_name(relative: Path) -> bool:
    for part in relative.parts:
        lowered = part.lower()
        if lowered in EXCLUDED_DIR_NAMES:
            return True
        if lowered == ".env" or lowered.startswith(".env."):
            return True
        if lowered.startswith("secret.") or lowered.startswith("secret-"):
            return True
        if lowered.startswith("private.") or lowered.startswith("private-"):
            return True
    return False


def should_include(path: Path, root: Path) -> bool:
    if not path.is_file():
        return False
    relative = path.relative_to(root)
    if not is_allowed_package_path(relative):
        return False
    if has_excluded_name(relative):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    if path.stat().st_size > MAX_PACKAGE_FILE_BYTES:
        return False
    return True


def iter_package_files(root: Path) -> list[Path]:
    validate_required_paths(root)
    return sorted(path for path in root.rglob("*") if should_include(path, root))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_zip_file(zip_file: zipfile.ZipFile, source: Path, archive_name: str) -> None:
    data = source.read_bytes()
    info = zipfile.ZipInfo(archive_name, FIXED_ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    zip_file.writestr(info, data)


def build_manifest(version: str, zip_path: Path, root: Path, files: list[Path]) -> dict[str, object]:
    file_entries = []
    for path in files:
        data = path.read_bytes()
        file_entries.append(
            {
                "path": path.relative_to(root).as_posix(),
                "size_bytes": len(data),
                "sha256": sha256_bytes(data),
            }
        )

    return {
        "package_name": PACKAGE_NAME,
        "version": version,
        "archive": {
            "name": zip_path.name,
            "size_bytes": zip_path.stat().st_size,
            "sha256": sha256_file(zip_path),
        },
        "included_paths": [path.as_posix() for path in REQUIRED_PACKAGE_PATHS],
        "excluded_rules": {
            "directories": sorted(EXCLUDED_DIR_NAMES),
            "suffixes": sorted(EXCLUDED_SUFFIXES),
            "env_files": [".env", ".env.*"],
            "max_file_bytes": MAX_PACKAGE_FILE_BYTES,
        },
        "files": file_entries,
    }


def build_package(version: str, root: Path, output_dir: Path | None = None) -> BuildOutputs:
    version = validate_version(version)
    root = root.resolve()
    output_dir = (output_dir or root / "dist").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    zip_path = output_dir / f"{PACKAGE_NAME}-{version}.zip"
    manifest_path = output_dir / f"package-manifest-{version}.json"
    zip_path.unlink(missing_ok=True)
    manifest_path.unlink(missing_ok=True)

    files = iter_package_files(root)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        for source in files:
            archive_name = source.relative_to(root).as_posix()
            write_zip_file(zip_file, source, archive_name)

    manifest = build_manifest(version, zip_path, root, files)
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return BuildOutputs(zip_path=zip_path, manifest_path=manifest_path)


def display_path(path: Path) -> Path:
    try:
        return path.relative_to(Path.cwd())
    except ValueError:
        return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a release zip package and manifest.")
    parser.add_argument("--version", required=True, help="Release version, for example v0.1.0")
    parser.add_argument("--root", default=Path(__file__).resolve().parents[1], type=Path)
    parser.add_argument("--output-dir", default=None, type=Path)
    args = parser.parse_args()

    try:
        outputs = build_package(args.version, args.root, args.output_dir)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Built {display_path(outputs.zip_path)}")
    print(f"Wrote {display_path(outputs.manifest_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
