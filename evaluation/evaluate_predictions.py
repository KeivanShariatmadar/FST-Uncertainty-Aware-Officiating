#!/usr/bin/env python3
"""Reproducible evaluation of audited FST/SSAC matched-event data.

This script evaluates *derived* matched events. It does not run the proprietary
FST implementation and does not infer ground truth from model predictions.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd


def safe_div(a, b):
    return float(a / b) if b else np.nan


def metrics(df):
    s = df["outcome"].astype(str).str.upper()
    tp, fp, fn = (int((s == x).sum()) for x in ("TP", "FP", "FN"))
    p = safe_div(tp, tp + fp)
    r = safe_div(tp, tp + fn)
    f1 = safe_div(2 * p * r, p + r) if np.isfinite(p) and np.isfinite(r) else np.nan
    return {"n": len(df), "TP": tp, "FP": fp, "FN": fn,
            "precision": p, "recall": r, "f1": f1}


def cluster_bootstrap(df, cluster, reps=2000, seed=2026):
    if cluster not in df or df[cluster].dropna().nunique() < 2:
        return pd.DataFrame()
    groups = list(df[cluster].dropna().unique())
    rng = np.random.default_rng(seed)
    rows = []
    for _ in range(reps):
        sampled = rng.choice(groups, len(groups), replace=True)
        boot = pd.concat([df[df[cluster] == g] for g in sampled], ignore_index=True)
        rows.append(metrics(boot))
    return pd.DataFrame(rows)


def risk_coverage(df, score_col, uncertainty_higher=True, points=101):
    x = df[df["outcome"].str.upper().isin(["TP", "FP"])].copy()
    x[score_col] = pd.to_numeric(x[score_col], errors="coerce")
    x = x.dropna(subset=[score_col])
    if x.empty:
        return pd.DataFrame()
    x["error"] = (x["outcome"].str.upper() == "FP").astype(int)
    x = x.sort_values(score_col, ascending=not uncertainty_higher)
    # least uncertain/reliable cases retained first
    if uncertainty_higher:
        x = x.sort_values(score_col, ascending=True)
    else:
        x = x.sort_values(score_col, ascending=False)
    ks = np.unique(np.maximum(1, np.ceil(np.linspace(1/points, 1, points) * len(x)).astype(int)))
    return pd.DataFrame([{"coverage": k/len(x), "retained_n": int(k),
                          "selective_risk": float(x.iloc[:k]["error"].mean())}
                         for k in ks])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("matched_csv", type=Path)
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--cluster", default="match_id")
    ap.add_argument("--bootstrap", type=int, default=2000)
    ap.add_argument("--uncertainty-col", default="model_uncertainty")
    ap.add_argument("--confidence-col", default="model_confidence")
    args = ap.parse_args()
    df = pd.read_csv(args.matched_csv)
    if "outcome" not in df:
        raise SystemExit("matched CSV must contain an 'outcome' column with TP/FP/FN")
    args.out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([metrics(df)]).to_csv(args.out / "overall_metrics.csv", index=False)
    boot = cluster_bootstrap(df, args.cluster, args.bootstrap)
    if not boot.empty:
        ci = []
        for m in ["precision", "recall", "f1"]:
            vals = boot[m].dropna()
            if len(vals):
                ci.append({"metric": m, "lower_95": vals.quantile(.025),
                           "upper_95": vals.quantile(.975), "bootstrap_reps": len(vals)})
        pd.DataFrame(ci).to_csv(args.out / "cluster_bootstrap_ci.csv", index=False)
    for col in ["action_type", "visibility", "contact_quality", "difficulty", "reference_ambiguity"]:
        if col in df:
            rows = []
            for val, g in df.groupby(col, dropna=False):
                z = metrics(g); z[col] = val; rows.append(z)
            pd.DataFrame(rows).to_csv(args.out / f"by_{col}.csv", index=False)
    if args.uncertainty_col in df:
        rc = risk_coverage(df, args.uncertainty_col, uncertainty_higher=True)
        if not rc.empty: rc.to_csv(args.out / "risk_coverage_uncertainty.csv", index=False)
    elif args.confidence_col in df:
        rc = risk_coverage(df, args.confidence_col, uncertainty_higher=False)
        if not rc.empty: rc.to_csv(args.out / "risk_coverage_confidence.csv", index=False)

if __name__ == "__main__":
    main()
