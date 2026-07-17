#!/usr/bin/env python3
"""Repository health checks for the Codex workbench."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MANIFEST_NAME = "repository-manifest.json"
SKIP_DIRS = {
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
    "