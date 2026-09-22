#!/usr/bin/env python3
"""Privacy-preserving inventory of a local FST source ZIP.

This utility is intended to be run locally against the private FST package.
It does not upload source code and never writes source-code snippets to its
reports. It records hashes, file metadata, dependency/model candidates, and
which files contain implementation-relevant signal terms.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath

TEXT_SUFFIXES = {
    ".py", ".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".ini",
    ".cfg", ".conf", ".sh", ".bat", ".ps1", ".csv",
}
MODEL_SUFFIXES = {".pt", ".pth", ".onnx", ".engine", ".weights", ".tflite", ".pb", ".pkl", ".joblib"}
DEPENDENCY_NAMES = {
    "requirements.txt", "pyproject.toml", "poetry.lock", "pipfile",
    "pipfile.lock", "environment.yml", "environment.yaml", "setup.py",
    "setup.cfg", "dockerfile", "docker-compose.yml", "docker-compose.yaml",
}
SENSITIVE_NAME_RE = re.compile(r"(^|/)(\\.env($|\\.)|.*(secret|token|credential|private[_-]?key).*)", re.I)

SIGNALS = {
    "uncertainty": r"\\buncertaint",
    "credal": r"\\bcredal",
    "random_set": r"random[ _-]?set",
    "interval": r"\\binterval",
    "ensemble": r"\\bensemble",
    "dropout": r"\\bdropout",
    "softmax": r"\\bsoftmax",
    "confidence": r"\\bconfiden",
    "threshold": r"\\bthreshold",
    "abstain_or_defer": r"\\b(abstain|defer|reject option|human review)\\b",
    "head_kick": r"head[ _-]?kick",
    "turning": r"\\bturning\\b|spin(n?ing)?",
    "pose": r"\\bpose\\b|keypoint|skeleton",
    "openpose": r"openpose",
    "mediapipe": r"mediapipe",
    "yolo": r"\\byolo",
    "pytorch": r"\\b(torch|pytorch)\\b",
    "tensorflow": r"\\b(tensorflow|keras)\\b",
    "onnx": r"\\bonnx",
    "opencv": r"\\b(cv2|opencv)\\b",
    "fps_or_frame": r"\\bfps\\b|frame[_ -]?rate|frame[_ -]?index",
    "latency_or_timing": r"\\blatency\\b|perf_counter|time\\.time|elapsed",
    "event_logic": r"\\bevent\\b|temporal|window|cooldown|debounce",
    "logging_or_export": r"\\b(csv|json|logger|logging|export|audit)\\b",
}
COMPILED = {k: re.compile(v, re.I) for k, v in SIGNALS.items()}


def sha256_stream(f) -> str:
    h = hashlib.sha256()
    while True:
        b = f.read(1024 * 1024)
        if not b:
            break
        h.update(b)
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_path", type=Path)
    ap.add_argument("--out", type=Path, default=Path("fst_package_audit"))
    ap.add_argument("--max-text-mb", type=float, default=5.0,
                    help="Maximum uncompressed size of a text member to scan.")
    args = ap.parse_args()

    if not args.zip_path.is_file():
        raise SystemExit(f"not found: {args.zip_path}")

    args.out.mkdir(parents=True, exist_ok=True)
    package_hash = hashlib.sha256(args.zip_path.read_bytes()).hexdigest()
    max_text = int(args.max_text_mb * 1024 * 1024)

    inventory = []
    signal_rows = []
    suffixes = Counter()
    dependency_files = []
    model_files = []
    possible_entrypoints = []
    sensitive_name_candidates = []

    with zipfile.ZipFile(args.zip_path, "r") as zf:
        bad = zf.testzip()
        for info in zf.infolist():
            if info.is_dir():
                continue

            p = PurePosixPath(info.filename)
            suffix = p.suffix.lower()
            suffixes[suffix or "(none)"] += 1
            lower_name = p.name.lower()

            with zf.open(info, "r") as fh:
                member_hash = sha256_stream(fh)

            row = {
                "path": info.filename,
                "size_bytes": info.file_size,
                "compressed_bytes": info.compress_size,
                "sha256": member_hash,
                "suffix": suffix,
            }
            inventory.append(row)

            if lower_name in DEPENDENCY_NAMES:
                dependency_files.append(info.filename)
            if suffix in MODEL_SUFFIXES:
                model_files.append(info.filename)
            if lower_name in {"main.py", "app.py", "run.py", "server.py", "infer.py", "inference.py", "pipeline.py"}:
                possible_entrypoints.append(info.filename)
            if SENSITIVE_NAME_RE.search(info.filename):
                sensitive_name_candidates.append(info.filename)

            if suffix not in TEXT_SUFFIXES or info.file_size > max_text:
                continue

            try:
                text = zf.read(info).decode("utf-8", errors="ignore")
            except Exception:
                continue

            for signal, pattern in COMPILED.items():
                count = len(pattern.findall(text))
                if count:
                    signal_rows.append({
                        "path": info.filename,
                        "signal": signal,
                        "match_count": count,
                    })

    with (args.out / "file_inventory.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["path", "size_bytes", "compressed_bytes", "sha256", "suffix"])
        w.writeheader()
        w.writerows(inventory)

    with (args.out / "implementation_signals.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["path", "signal", "match_count"])
        w.writeheader()
        w.writerows(signal_rows)

    manifest = {
        "source_zip_name": args.zip_path.name,
        "source_zip_size_bytes": args.zip_path.stat().st_size,
        "source_zip_sha256": package_hash,
        "zip_integrity_bad_member": bad,
        "file_count": len(inventory),
        "suffix_counts": dict(sorted(suffixes.items())),
        "dependency_files": sorted(dependency_files),
        "model_or_weight_candidates": sorted(model_files),
        "possible_entrypoints": sorted(possible_entrypoints),
        "sensitive_filename_candidates": sorted(sensitive_name_candidates),
        "signal_vocabulary": sorted(SIGNALS),
        "privacy_note": (
            "Reports contain metadata, hashes, filenames and signal counts only. "
            "No source-code snippets or secret values are written."
        ),
    }
    (args.out / "package_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\\n", encoding="utf-8"
    )

    print(json.dumps(manifest, indent=2))
    print(f"\\nWrote audit reports to {args.out}")
    if sensitive_name_candidates:
        print("WARNING: sensitive-looking filenames were detected; inspect locally and do not publish secrets.")


if __name__ == "__main__":
    main()
