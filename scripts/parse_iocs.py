#!/usr/bin/env python3
"""
parse_iocs.py

Training-friendly IOC parsing helper.

Reads a CSV of indicators and prints:
- a quick summary by type
- optional normalized output for downstream tools

This is intentionally lightweight and defensive:
- accepts a minimal CSV schema
- best-effort parsing
- no network calls

Expected input columns (recommended):
  type,value,source,confidence,notes

Example types:
  ip, domain, url, sha256, email

"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


VALID_TYPES = {"ip", "domain", "url", "sha256", "email", "file", "process"}


@dataclass(frozen=True)
class IOC:
    ioc_type: str
    value: str
    source: str = ""
    confidence: str = ""
    notes: str = ""


def normalize_type(raw: str) -> str:
    t = (raw or "").strip().lower()
    # A few friendly aliases
    aliases = {
        "hash": "sha256",
        "sha-256": "sha256",
        "hostname": "domain",
        "fqdn": "domain",
    }
    t = aliases.get(t, t)
    return t


def normalize_value(ioc_type: str, raw: str) -> str:
    v = (raw or "").strip()
    if ioc_type in {"domain", "email"}:
        v = v.lower()
    if ioc_type == "url":
        # Keep it simple; do not attempt full URL parsing in a training repo
        v = v.strip()
    return v


def read_iocs(path: Path) -> List[IOC]:
    if not path.exists():
        raise FileNotFoundError(f"Input not found: {path}")

    iocs: List[IOC] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV has no headers")

        for row in reader:
            ioc_type = normalize_type(row.get("type", ""))
            value = normalize_value(ioc_type, row.get("value", ""))

            if not ioc_type or not value:
                # Skip blank rows quietly
                continue

            iocs.append(
                IOC(
                    ioc_type=ioc_type,
                    value=value,
                    source=(row.get("source") or "").strip(),
                    confidence=(row.get("confidence") or "").strip(),
                    notes=(row.get("notes") or "").strip(),
                )
            )
    return iocs


def summarize(iocs: Iterable[IOC]) -> str:
    items = list(iocs)
    by_type = Counter(i.ioc_type for i in items)
    total = len(items)

    lines: List[str] = []
    lines.append("IOC Summary")
    lines.append("=" * 40)
    lines.append(f"Total indicators: {total}")
    lines.append("")

    if total == 0:
        lines.append("No indicators found.")
        return "\n".join(lines)

    lines.append("Counts by type:")
    for t, n in sorted(by_type.items(), key=lambda x: (-x[1], x[0])):
        label = t if t in VALID_TYPES else f"{t} (unrecognized)"
        lines.append(f"  - {label}: {n}")
    lines.append("")

    # Show a small preview list (deduped)
    lines.append("Preview (deduped, first 20):")
    seen: set[Tuple[str, str]] = set()
    shown = 0
    for i in items:
        key = (i.ioc_type, i.value)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"  - {i.ioc_type}: {i.value}")
        shown += 1
        if shown >= 20:
            break

    return "\n".join(lines)


def write_normalized(iocs: Iterable[IOC], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["type", "value", "source", "confidence", "notes"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in iocs:
            writer.writerow(
                {
                    "type": i.ioc_type,
                    "value": i.value,
                    "source": i.source,
                    "confidence": i.confidence,
                    "notes": i.notes,
                }
            )


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Parse and summarize IOC CSV files (training helper).")
    p.add_argument("--input", "-i", required=True, help="Path to IOC CSV (e.g., data/sample_iocs.csv)")
    p.add_argument("--summary", action="store_true", help="Print a summary to stdout")
    p.add_argument("--normalize-out", help="Write a normalized CSV to this path (optional)")
    args = p.parse_args(argv)

    try:
        iocs = read_iocs(Path(args.input))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    if args.summary:
        print(summarize(iocs))

    if args.normalize_out:
        try:
            write_normalized(iocs, Path(args.normalize_out))
        except Exception as e:
            print(f"Error writing normalized output: {e}", file=sys.stderr)
            return 3

    # If neither option was selected, default to summary for convenience
    if not args.summary and not args.normalize_out:
        print(summarize(iocs))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
