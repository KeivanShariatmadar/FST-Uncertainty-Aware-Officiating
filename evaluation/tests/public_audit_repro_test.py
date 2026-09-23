#!/usr/bin/env python3
"""Reproduce the public candidate audit and verify the checked-in evidence tables."""
from pathlib import Path
import math
import subprocess
import sys
import tempfile
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
EVAL = ROOT / "evaluation"
DATA = ROOT / "data" / "derived"


def summary_map(path: Path) -> dict[str, str]:
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    return dict(zip(df["metric"], df["value"]))


def close(a: str, b: str, tol: float = 1e-12) -> bool:
    try:
        return math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)
    except ValueError:
        return str(a) == str(b)


def keyed_counts(path: Path, keys: list[str]) -> dict[tuple[str, ...], int]:
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    return {
        tuple(str(row[k]) for k in keys): int(float(row["count"]))
        for _, row in df.iterrows()
    }


def main() -> None:
    source = DATA / "annotation_candidate_records_deidentified.csv"

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

        got_summary = summary_map(out / "annotation_audit_summary.csv")
        ref_summary = summary_map(DATA / "annotation_audit_summary.csv")
        core_metrics = [
            "raw_records",
            "canonical_records",
            "raw_unique_match_ids",
            "raw_unique_bout_clusters",
            "raw_true_positive_labels",
            "raw_false_positive_labels",
            "canonical_true_positive_labels",
            "canonical_false_positive_labels",
            "canonical_candidate_confirmation_rate",
            "canonical_candidate_confirmation_cluster_count",
            "canonical_candidate_confirmation_cluster_jackknife_se",
            "canonical_candidate_confirmation_cluster_jackknife_95_low",
            "canonical_candidate_confirmation_cluster_jackknife_95_high",
            "exact_duplicate_match_clip_keys",
            "dominant_four_joint_patterns_records",
            "dominant_four_joint_patterns_share",
            "fp_rows_with_medium_hard_uncertain_uncertain_partial_occlusion_signature",
            "good_visibility_rows",
            "moderate_visibility_rows",
            "partial_occlusion_rows",
            "false_positive_partial_occlusion_rows",
            "uncertain_event_label_rows",
            "uncertain_contact_rows",
        ]
        for metric in core_metrics:
            assert metric in got_summary and metric in ref_summary, metric
            assert close(got_summary[metric], ref_summary[metric]), (
                metric, got_summary[metric], ref_summary[metric]
            )

        got_cat = keyed_counts(out / "annotation_category_counts.csv", ["field", "value"])
        ref_cat = keyed_counts(DATA / "annotation_category_counts.csv", ["field", "value"])
        assert got_cat == ref_cat

        got_patterns = keyed_counts(
            out / "annotation_joint_patterns.csv",
            ["label", "human_confidence", "difficulty", "event_label", "contact", "visibility"],
        )
        ref_patterns = keyed_counts(
            DATA / "annotation_joint_patterns.csv",
            ["label", "human_confidence", "difficulty", "event_label", "contact", "visibility"],
        )
        assert got_patterns == ref_patterns

    print("Public annotation audit reproduction test passed.")


if __name__ == "__main__":
    main()
