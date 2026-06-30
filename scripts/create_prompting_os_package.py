#!/usr/bin/env python3
"""Build a deterministic Prompting OS release ZIP and manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from typing import NamedTuple

PACKAGE_STEM = "prompting-os"
DEFAULT_VERSION = "v1"
PACKAGE_ROOT = "Prompting_OS_v1"
FIXED_ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
MAX_PACKAGE_FILE_BYTES = 5_000_000

VERSION_PATTERN = re.compile(r"v?\d+(?:\.\d+){0,2}(?:-[0-9A-Za-z.-]+)?")

EXCLUDED_DIR_NAMES = {
    ".cache",
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "logs",
    "node_modules",
    "outputs",
    "private",
    "secret",
    "secrets",
    "venv",
}

EXCLUDED_SUFFIXES = {
    ".7z",
    ".bak",
    ".bin",
    ".db",
    ".gguf",
    ".gz",
    ".key",
    ".log",
    ".p12",
    ".pem",
    ".pyc",
    ".pyo",
    ".rar",
    ".sqlite",
    ".tar",
    ".tgz",
    ".tmp",
    ".zip",
}


class PackageOutputs(NamedTuple):
    zip_path: Path
    manifest_path: Path


def normalize_version(version: str) -> str:
    """Return a safe version label such as v1 or v1.2.0."""
    label = version.strip()
    if not VERSION_PATTERN.fullmatch(label):
        raise ValueError("Version must look like v1, v1.2.0, or v1.2.0-beta.1.")
    if ".." in label:
        raise ValueError("Version must not contain consecutive dots.")
    if not label.startswith("v"):
        label = f"v{label}"
    return label


def resolve_path(base: Path, path: Path | None, default: Path) -> Path:
    """Resolve optional CLI paths relative to the repository root."""
    if path is None:
        return default.resolve()
    if path.is_absolute():
        return path.resolve()
    return (base / path).resolve()


def display_relative(path: Path, root: Path) -> str:
    """Render paths relative to the repo root so manifests stay public-safe."""
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.name


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


def should_include(path: Path, source_dir: Path) -> bool:
    if not path.is_file():
        return False
    relative = path.relative_to(source_dir)
    if has_excluded_name(relative):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    if path.stat().st_size > MAX_PACKAGE_FILE_BYTES:
        return False
    return True


def iter_source_files(source_dir: Path) -> list[Path]:
    return sorted(path for path in source_dir.rglob("*") if should_include(path, source_dir))


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


def build_manifest(
    *,
    root: Path,
    source_dir: Path,
    zip_path: Path,
    version: str,
    files: list[Path],
) -> dict[str, object]:
    file_entries = []
    for path in files:
        data = path.read_bytes()
        file_entries.append(
            {
                "path": display_relative(path, root),
                "archive_path": (Path(PACKAGE_ROOT) / path.relative_to(source_dir)).as_posix(),
                "size_bytes": len(data),
                "sha256": sha256_bytes(data),
            }
        )

    return {
        "package_name": PACKAGE_STEM,
        "version": version,
        "source_dir": display_relative(source_dir, root),
        "package_root": PACKAGE_ROOT,
        "archive": {
            "name": zip_path.name,
            "size_bytes": zip_path.stat().st_size,
            "sha256": sha256_file(zip_path),
        },
        "excluded_rules": {
            "directories": sorted(EXCLUDED_DIR_NAMES),
            "suffixes": sorted(EXCLUDED_SUFFIXES),
            "env_files": [".env", ".env.*"],
            "max_file_bytes": MAX_PACKAGE_FILE_BYTES,
        },
        "files": file_entries,
    }


def build_package(
    root: Path,
    version: str = DEFAULT_VERSION,
    source_dir: Path | None = None,
    output_dir: Path | None = None,
) -> PackageOutputs:
    """Build the Prompting OS package from source docs under docs/prompting-os."""
    root = root.resolve()
    version = normalize_version(version)
    source_dir = resolve_path(root, source_dir, root / "docs" / "prompting-os")
    output_dir = resolve_path(root, output_dir, root / "release" / "packages")

    if not source_dir.is_dir():
        raise FileNotFoundError(f"Missing source directory: {display_relative(source_dir, root)}")
    try:
        source_dir.relative_to(root)
    except ValueError as exc:
        raise ValueError("source_dir must be inside the repository root") from exc

    files = iter_source_files(source_dir)
    if not files:
        raise FileNotFoundError(f"No packageable files found in {display_relative(source_dir, root)}")

    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f"{PACKAGE_STEM}-{version}.zip"
    manifest_path = output_dir / f"{PACKAGE_STEM}-{version}-manifest.json"
    zip_path.unlink(missing_ok=True)
    manifest_path.unlink(missing_ok=True)

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        for source in files:
            archive_name = (Path(PACKAGE_ROOT) / source.relative_to(source_dir)).as_posix()
            write_zip_file(zip_file, source, archive_name)

    manifest = build_manifest(
        root=root,
        source_dir=source_dir,
        zip_path=zip_path,
        version=version,
        files=files,
    )
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return PackageOutputs(zip_path=zip_path, manifest_path=manifest_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the Prompting OS release ZIP and manifest.")
    parser.add_argument("--root", default=Path(__file__).resolve().parents[1], type=Path)
    parser.add_argument("--version", default=DEFAULT_VERSION, help="Version label, for example v1 or v1.1.0")
    parser.add_argument("--source-dir", default=None, type=Path, help="Source directory inside the repository")
    parser.add_argument("--output-dir", default=None, type=Path, help="Output directory for the zip and manifest")
    args = parser.parse_args()

    try:
        outputs = build_package(
            root=args.root,
            version=args.version,
            source_dir=args.source_dir,
            output_dir=args.output_dir,
        )
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    root = args.root.resolve()
    print(f"Built {display_relative(outputs.zip_path, root)}")
    print(f"Wrote {display_relative(outputs.manifest_path, root)}")
    print(f"SHA256 {sha256_file(outputs.zip_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
