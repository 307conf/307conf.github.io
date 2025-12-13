#!/usr/bin/env python3
"""Backfill English content with Portuguese pages to avoid 404s.

Scans `content/pt-br/` and, for any file missing under `content/en/` at
the same relative path, copies the Portuguese file over.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PT_ROOT = ROOT / "content" / "pt-br"
EN_ROOT = ROOT / "content" / "en"


def iter_source_files(extensions: set[str]) -> list[Path]:
    files: list[Path] = []
    for path in PT_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if extensions and path.suffix.lower() not in extensions:
            continue
        files.append(path)
    return files


def backfill(*, extensions: set[str], dry_run: bool) -> None:
    if not PT_ROOT.exists():
        raise SystemExit(f"Portuguese content dir not found: {PT_ROOT}")
    if not EN_ROOT.exists():
        raise SystemExit(f"English content dir not found: {EN_ROOT}")

    sources = iter_source_files(extensions)
    for src in sources:
        rel = src.relative_to(PT_ROOT)
        dst = EN_ROOT / rel
        if dst.exists():
            continue

        if dry_run:
            print(f"[dry-run] would copy {rel} -> {dst.relative_to(ROOT)}")
            continue

        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"[copy] {rel} -> {dst.relative_to(ROOT)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only report files that would be copied.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Copy all file types (default: only .md).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    extensions = set() if args.all else {".md"}
    backfill(extensions=extensions, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
