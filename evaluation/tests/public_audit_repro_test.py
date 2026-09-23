#!/usr/bin/env python3
"""Reproduce the public candidate audit and compare key outputs to the repository."""
from pathlib import Path
import subprocess
import sys
import tempfile
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
EVAL = ROOT / "evaluation"
DATA = ROOT / "data" / "derived"


def normalized_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    return df.sort_values(list(df.columns), kind="stable").reset_index(drop=True)


def main() -> None:
    source = DATA / "annotation_candidate_records_deidentified.csv"
    expected = [
        "annotation_audit_summary.csv",
        "annotation_category_counts.csv",
        "annotation_joint_patterns.csv",
        "annotation_stratified_confirmation.csv",
    ]

    with tempfile.TemporaryDirectory() as td:
        out = Path(td)
        subprocess.run(
            [
                sys.executable,
                str(EVAL / "audit_candidate_annotations.py"),
                str(source),
                "--out",
                str(out),
            ],
            check=True,
            cwd=ROOT,
        )

        for name in expected:
            got = normalized_csv(out / name)
            ref = normalized_csv(DATA / name)
            try:
                pd.testing.assert_frame_equal(got, ref, check_dtype=False)
            except AssertionError as exc:
                raise AssertionError(f"reproduced {name} differs from repository copy") from exc

    print("Public annotation audit reproduction test passed.")


if __name__ == "__main__":
    main()
