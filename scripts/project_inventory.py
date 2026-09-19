#!/usr/bin/env python3
"""Create a concise inventory of files relevant to an academic paper project."""

from __future__ import annotations

import argparse
import os
import sys
from collections import Counter
from pathlib import Path

INTERESTING_SUFFIXES = {
    ".tex", ".bib", ".pdf", ".png", ".jpg", ".jpeg", ".svg", ".eps",
    ".csv", ".tsv", ".json", ".jsonl", ".txt", ".log", ".yaml", ".yml",
    ".toml", ".ini", ".md", ".rst", ".sty", ".cls", ".bst", ".aux",
    ".bbl", ".blg", ".fls", ".fdb_latexmk", ".out", ".toc",
    ".py", ".sh", ".r", ".m", ".c", ".cc", ".cpp", ".h", ".hpp",
    ".java", ".ipynb", ".npy", ".npz", ".parquet", ".pkl", ".pickle",
}

INTERESTING_NAMES = {
    "readme", "readme.md", "makefile", "latexmkrc", ".latexmkrc", "requirements.txt",
    "environment.yml", "environment.yaml", "pyproject.toml", "setup.py",
    "conda-lock.yml", "poetry.lock",
}

IGNORE_DIRS = {
    ".git", ".hg", ".svn", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".cache", "node_modules", "venv", ".venv", "env", "dist", ".idea",
    ".vscode", ".tox", ".ruff_cache",
}

LARGE_FILE_SUFFIXES = {
    ".ckpt", ".pth", ".pt", ".bin", ".safetensors", ".onnx", ".h5", ".hdf5",
}


def should_include(path: Path) -> bool:
    """Return whether a file is useful for a paper-project audit."""
    name = path.name.lower()
    if name in INTERESTING_NAMES:
        return True
    return path.suffix.lower() in INTERESTING_SUFFIXES


def inventory(root: Path, max_files: int) -> tuple[list[Path], Counter[str], list[Path], int]:
    """List paths without opening project files, importing modules, or following links."""
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"Not a directory: {root}")
    if max_files < 1:
        raise ValueError("--max-files must be at least 1")

    files: list[Path] = []
    skipped_large: list[Path] = []
    counts: Counter[str] = Counter()

    def report_error(error: OSError) -> None:
        print(f"Warning: unable to inspect {error.filename}: {error.strerror}", file=sys.stderr)

    # Prune excluded trees before descending; rglob would still walk their contents.
    for directory, dirnames, filenames in os.walk(root, followlinks=False, onerror=report_error):
        current = Path(directory)
        dirnames[:] = sorted(
            name for name in dirnames
            if name not in IGNORE_DIRS and not (current / name).is_symlink()
        )
        for name in sorted(filenames):
            path = current / name
            try:
                if path.is_symlink() or not path.is_file():
                    continue
                rel = path.relative_to(root)
                if path.suffix.lower() in LARGE_FILE_SUFFIXES:
                    skipped_large.append(rel)
                    continue
                if should_include(path):
                    files.append(rel)
                    counts[path.suffix.lower() or path.name.lower()] += 1
            except OSError as error:
                report_error(error)

    files.sort(key=lambda p: (len(p.parts), str(p).lower()))
    skipped_large.sort(key=str)
    return files[:max_files], counts, skipped_large, len(files)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Paper-project root directory")
    parser.add_argument("--max-files", type=int, default=500, help="Maximum number of paths to print")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")
    if args.max_files < 1:
        raise SystemExit("--max-files must be at least 1")

    files, counts, skipped_large, total_matches = inventory(root, args.max_files)

    print(f"Project root: {root}")
    print(f"Relevant files found: {total_matches}")
    print(f"Relevant files shown: {len(files)}")

    if counts:
        print("Type counts:")
        for suffix, count in sorted(counts.items()):
            print(f"  {suffix}: {count}")

    print("Files:")
    for rel in files:
        print(f"  {rel}")

    if total_matches > len(files):
        print(f"Output truncated: {total_matches - len(files)} additional relevant files not shown")

    if skipped_large:
        print(f"Large model/checkpoint artifacts skipped: {len(skipped_large)}")


if __name__ == "__main__":
    main()
