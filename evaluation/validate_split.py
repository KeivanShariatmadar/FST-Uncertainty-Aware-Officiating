#!/usr/bin/env python3
"""Validate FST benchmark split manifest for bout/match leakage."""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

REQUIRED = ["evaluation_id", "match_id", "bout_cluster_id", "split"]
ALLOWED = {"train", "validation", "val", "test"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    args = ap.parse_args()

    df = pd.read_csv(args.manifest, dtype=str, keep_default_na=False)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise SystemExit(f"missing required columns: {missing}")

    if df["evaluation_id"].duplicated().any():
        bad = df.loc[df["evaluation_id"].duplicated(False), "evaluation_id"].unique()
        raise SystemExit(f"duplicate evaluation_id values: {bad[:10].tolist()}")

    splits = df["split"].str.strip().str.lower()
    invalid = sorted(set(splits) - ALLOWED)
    if invalid:
        raise SystemExit(f"invalid split values: {invalid}")

    # normalize val -> validation
    df = df.copy()
    df["split_norm"] = splits.replace({"val": "validation"})

    bout_leak = (
        df.groupby("bout_cluster_id")["split_norm"].nunique()
          .loc[lambda x: x > 1]
    )
    match_leak = (
        df.groupby("match_id")["split_norm"].nunique()
          .loc[lambda x: x > 1]
    )

    print("rows:", len(df))
    print("unique match_ids:", df["match_id"].nunique())
    print("unique bout_cluster_ids:", df["bout_cluster_id"].nunique())
    print("\ncounts by split:")
    print(df.groupby("split_norm").size().to_string())

    if len(bout_leak):
        print("\nERROR: bout_cluster_id appears in more than one split:")
        print(bout_leak.to_string())
    if len(match_leak):
        print("\nERROR: match_id appears in more than one split:")
        print(match_leak.to_string())

    if len(bout_leak) or len(match_leak):
        raise SystemExit(2)

    if "athlete_id" in df.columns and df["athlete_id"].str.len().gt(0).any():
        athlete_splits = (
            df[df["athlete_id"].str.len().gt(0)]
            .groupby("athlete_id")["split_norm"].agg(lambda x: sorted(set(x)))
        )
        overlapping = athlete_splits[athlete_splits.map(len) > 1]
        print(f"\nathletes spanning multiple splits: {len(overlapping)}")
        if len(overlapping):
            print("Athlete overlap is a reporting item, not an automatic failure under the primary bout-held-out regime.")

    print("\nPASS: no match/bout split leakage detected.")


if __name__ == "__main__":
    main()
