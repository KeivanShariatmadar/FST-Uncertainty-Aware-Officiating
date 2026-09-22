#!/usr/bin/env python3
"""Reproduce the public FST candidate-annotation audit from the released CSV.

This script analyses human candidate-validation/context annotations. It does
NOT estimate recall/F1 and it does NOT interpret human confidence as FST model
uncertainty.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import json
import pandas as pd

REQUIRED = [
    "record_id", "match_id", "bout_cluster_id", "clip_name", "label",
    "human_confidence", "difficulty", "event_label", "contact", "visibility",
    "duplicate_key", "canonical_record", "bookkeeping_flag",
    "analysis_inclusion", "provenance_role",
]

DOMINANT_FIELDS = ["label", "human_confidence", "difficulty", "event_label", "contact", "visibility"]


def as_bool(s: pd.Series) -> pd.Series:
    return s.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def value_counts_table(df: pd.DataFrame, field: str) -> pd.DataFrame:
    x = (
        df[field]
        .fillna("(missing)")
        .astype(str)
        .value_counts(dropna=False)
        .rename_axis("value")
        .reset_index(name="count")
    )
    x.insert(0, "field", field)
    x["share"] = x["count"] / len(df) if len(df) else float("nan")
    return x


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate_csv", type=Path)
    ap.add_argument("--out", type=Path, default=Path("candidate_audit_results"))
    args = ap.parse_args()

    df = pd.read_csv(args.candidate_csv, dtype=str, keep_default_na=False)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise SystemExit(f"missing required columns: {missing}")

    args.out.mkdir(parents=True, exist_ok=True)

    canonical = df[as_bool(df["canonical_record"])].copy()
    if canonical.empty:
        raise SystemExit("no canonical records found")

    key_counts = df.groupby(["match_id", "clip_name"], dropna=False).size()
    duplicate_keys = key_counts[key_counts > 1]

    raw_labels = df["label"].value_counts()
    canonical_labels = canonical["label"].value_counts()

    patterns = (
        df.groupby(DOMINANT_FIELDS, dropna=False)
          .size()
          .reset_index(name="count")
          .sort_values("count", ascending=False, kind="stable")
          .reset_index(drop=True)
    )
    patterns["share"] = patterns["count"] / len(df)

    dominant_four = int(patterns.head(4)["count"].sum())

    fp_mask = df["label"].eq("False Positive")
    fp_signature = (
        fp_mask
        & df["human_confidence"].eq("Medium")
        & df["difficulty"].eq("Hard")
        & df["event_label"].eq("uncertain")
        & df["contact"].eq("uncertain")
        & df["visibility"].eq("partial_occlusion")
    )

    tp_c = int(canonical_labels.get("True Positive", 0))
    fp_c = int(canonical_labels.get("False Positive", 0))
    # Delete-one-bout cluster jackknife for the descriptive candidate-confirmation ratio.
    # This accounts for within-bout dependence without pretending that the
    # candidate sample is a complete event census.
    total_n = len(canonical)
    total_tp = tp_c
    clusters = []
    for cluster_id, g in canonical.groupby("bout_cluster_id", dropna=False):
        g_tp = int(g["label"].eq("True Positive").sum())
        clusters.append((cluster_id, len(g), g_tp))
    loo = [
        (total_tp - g_tp) / (total_n - g_n)
        for _, g_n, g_tp in clusters
        if total_n > g_n
    ]
    g_count = len(loo)
    jack_mean = sum(loo) / g_count
    jack_var = ((g_count - 1) / g_count) * sum((x - jack_mean) ** 2 for x in loo)
    jack_se = jack_var ** 0.5
    confirmation = total_tp / total_n
    jack_lo = max(0.0, confirmation - 1.96 * jack_se)
    jack_hi = min(1.0, confirmation + 1.96 * jack_se)

    summary = [
        ("raw_records", len(df), "records", "released raw de-identified candidate table"),
        ("canonical_records", len(canonical), "records", "canonical_record=true"),
        ("raw_unique_match_ids", df["match_id"].nunique(), "match IDs", "source identifiers; not necessarily unique bouts"),
        ("raw_unique_bout_clusters", df["bout_cluster_id"].nunique(), "bout clusters", "uses linked cluster where source says two IDs are one bout"),
        ("raw_true_positive_labels", int(raw_labels.get("True Positive", 0)), "candidate labels", "human candidate-validation label"),
        ("raw_false_positive_labels", int(raw_labels.get("False Positive", 0)), "candidate labels", "human candidate-validation label"),
        ("canonical_true_positive_labels", tp_c, "candidate labels", "after exact duplicate exclusion"),
        ("canonical_false_positive_labels", fp_c, "candidate labels", "after exact duplicate exclusion"),
        ("canonical_candidate_confirmation_rate", confirmation, "proportion", "TP/(TP+FP) within selected candidate population; not recall/F1"),
        ("canonical_candidate_confirmation_cluster_count", g_count, "bout clusters", "delete-one-cluster jackknife uses bout_cluster_id"),
        ("canonical_candidate_confirmation_cluster_jackknife_se", jack_se, "proportion", "delete-one-bout jackknife standard error"),
        ("canonical_candidate_confirmation_cluster_jackknife_95_low", jack_lo, "proportion", "normal 95% interval using cluster-jackknife SE"),
        ("canonical_candidate_confirmation_cluster_jackknife_95_high", jack_hi, "proportion", "normal 95% interval using cluster-jackknife SE"),
        ("exact_duplicate_match_clip_keys", len(duplicate_keys), "keys", "match_id + clip_name with count > 1"),
        ("dominant_four_joint_patterns_records", dominant_four, "records", "top four label/confidence/difficulty/event/contact patterns"),
        ("dominant_four_joint_patterns_share", dominant_four / len(df), "proportion", "top-four share of raw candidate table"),
        ("fp_rows_with_medium_hard_uncertain_uncertain_partial_occlusion_signature", int(fp_signature.sum()), "records", "descriptive structural regularity"),
        ("good_visibility_rows", int(df["visibility"].eq("good").sum()), "records", "human/contextual visibility annotation"),
        ("moderate_visibility_rows", int(df["visibility"].eq("moderate").sum()), "records", "human/contextual visibility annotation"),
        ("partial_occlusion_rows", int(df["visibility"].eq("partial_occlusion").sum()), "records", "human/contextual visibility annotation"),
        ("false_positive_partial_occlusion_rows", int((fp_mask & df["visibility"].eq("partial_occlusion")).sum()), "records", "descriptive structural regularity"),
        ("uncertain_event_label_rows", int(df["event_label"].eq("uncertain").sum()), "records", "human/contextual event annotation"),
        ("uncertain_contact_rows", int(df["contact"].eq("uncertain").sum()), "records", "human/contextual contact annotation"),
    ]
    summary_df = pd.DataFrame(summary, columns=["metric", "value", "unit", "interpretation"])

    category_tables = [
        value_counts_table(df, f)
        for f in ["label", "human_confidence", "difficulty", "event_label", "contact", "visibility"]
    ]
    category_df = pd.concat(category_tables, ignore_index=True)

    dup_df = duplicate_keys.rename("count").reset_index()
    flagged_df = df[
        df["bookkeeping_flag"].astype(str).str.len().gt(0)
        | as_bool(df["duplicate_key"])
    ].copy()

    summary_df.to_csv(args.out / "annotation_audit_summary.csv", index=False)
    category_df.to_csv(args.out / "annotation_category_counts.csv", index=False)
    patterns.to_csv(args.out / "annotation_joint_patterns.csv", index=False)
    strata = []
    for field in ["visibility", "difficulty", "human_confidence", "event_label", "contact"]:
        for value, g in canonical.groupby(field, dropna=False):
            labels = g["label"].value_counts()
            tp = int(labels.get("True Positive", 0))
            fp = int(labels.get("False Positive", 0))
            denom = tp + fp
            strata.append({
                "field": field,
                "value": value,
                "n": len(g),
                "tp_labelled": tp,
                "fp_labelled": fp,
                "candidate_confirmation_rate": (tp / denom) if denom else float("nan"),
                "interpretation": (
                    "human confidence, not model uncertainty"
                    if field == "human_confidence"
                    else "descriptive only; annotation fields are structurally coupled"
                ),
            })
    pd.DataFrame(strata).to_csv(
        args.out / "annotation_stratified_confirmation.csv", index=False
    )
    dup_df.to_csv(args.out / "annotation_duplicate_keys.csv", index=False)
    flagged_df.to_csv(args.out / "annotation_flagged_records.csv", index=False)

    machine = {
        row["metric"]: row["value"]
        for row in summary_df.to_dict(orient="records")
    }
    (args.out / "annotation_audit_summary.json").write_text(
        json.dumps(machine, indent=2) + "\n", encoding="utf-8"
    )

    print(summary_df.to_string(index=False))
    print("\nIMPORTANT: candidate-confirmation rate is descriptive for the selected "
          "candidate population and must not be reported as recall/F1.")


if __name__ == "__main__":
    main()
