#!/usr/bin/env python3
"""One-command public reproducibility runner for the FST SSAC27 package.

Always reproduces the released candidate-annotation audit. If independently
frozen ground-truth and prediction files are present, it also runs the
registered event-level benchmark. It never fabricates missing benchmark files.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "evaluation"
DATA = ROOT / "data" / "derived"


def run(cmd: list[str]) -> None:
    print("+", " ".join(str(x) for x in cmd))
    subprocess.run([str(x) for x in cmd], check=True, cwd=ROOT)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=ROOT / "reproduced_results")
    ap.add_argument("--tolerance-s", type=float, default=None,
                    help="Required only when running the independent event benchmark.")
    ap.add_argument("--class-mode", choices=["exact", "ignore"], default="exact")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)

    candidate_csv = DATA / "annotation_candidate_records_deidentified.csv"
    if not candidate_csv.exists():
        raise SystemExit(f"missing public candidate data: {candidate_csv}")

    run([
        sys.executable,
        EVAL / "audit_candidate_annotations.py",
        candidate_csv,
        "--out",
        args.out / "candidate_audit",
    ])

    gt = DATA / "ground_truth_events.csv"
    pred = DATA / "fst_ssac_predictions.csv"

    if gt.exists() and pred.exists():
        if args.tolerance_s is None:
            raise SystemExit(
                "ground-truth and prediction files are present, but --tolerance-s "
                "was not supplied. The matching tolerance must be declared explicitly."
            )
        matched = args.out / "matched_events.csv"
        run([
            sys.executable,
            EVAL / "match_events.py",
            gt,
            pred,
            "--tolerance-s",
            str(args.tolerance_s),
            "--class-mode",
            args.class_mode,
            "--output",
            matched,
        ])
        run([
            sys.executable,
            EVAL / "evaluate_predictions.py",
            matched,
            "--out",
            args.out / "event_benchmark",
        ])
        print("\nIndependent event benchmark completed.")
    else:
        print(
            "\nIndependent event benchmark not run: ground_truth_events.csv and/or "
            "fst_ssac_predictions.csv is absent. This is expected until the frozen "
            "model benchmark is available."
        )

    print(f"\nReproducibility outputs: {args.out}")


if __name__ == "__main__":
    main()
