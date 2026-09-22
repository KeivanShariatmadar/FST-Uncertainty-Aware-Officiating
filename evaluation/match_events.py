#!/usr/bin/env python3
"""Deterministic one-to-one temporal event matching for the FST/SSAC benchmark.

Ground truth and model predictions must be produced independently. This script
derives TP/FP/FN only after both layers are frozen.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

GT_REQUIRED = ["event_id", "match_id", "timestamp_s", "action_type"]
PRED_REQUIRED = ["prediction_id", "match_id", "timestamp_s", "predicted_action_type"]


def require(df: pd.DataFrame, cols: list[str], name: str) -> None:
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise SystemExit(f"{name}: missing required columns {missing}")


def norm_action(x) -> str:
    return str(x).strip().lower().replace(" ", "_")


def match_events(gt: pd.DataFrame, pred: pd.DataFrame, tolerance_s: float, class_mode: str = "exact") -> pd.DataFrame:
    require(gt, GT_REQUIRED, "ground truth")
    require(pred, PRED_REQUIRED, "predictions")
    if tolerance_s <= 0:
        raise ValueError("tolerance_s must be > 0")
    if class_mode not in {"exact", "ignore"}:
        raise ValueError("class_mode must be 'exact' or 'ignore'")

    gt = gt.copy()
    pred = pred.copy()
    gt["timestamp_s"] = pd.to_numeric(gt["timestamp_s"], errors="raise")
    pred["timestamp_s"] = pd.to_numeric(pred["timestamp_s"], errors="raise")
    if gt["event_id"].astype(str).duplicated().any():
        raise SystemExit("ground truth contains duplicate event_id")
    if pred["prediction_id"].astype(str).duplicated().any():
        raise SystemExit("predictions contain duplicate prediction_id")

    rows = []
    all_matches = sorted(set(gt["match_id"].astype(str)) | set(pred["match_id"].astype(str)))

    gt_context = ["visibility", "contact_quality", "difficulty", "reference_ambiguity", "bout_cluster_id"]
    pred_context = ["model_confidence", "model_uncertainty", "model_version", "inference_config_id"]

    for match_id in all_matches:
        g = gt[gt["match_id"].astype(str) == match_id].reset_index(drop=True)
        p = pred[pred["match_id"].astype(str) == match_id].reset_index(drop=True)

        candidates = []
        for gi, gr in g.iterrows():
            ga = norm_action(gr["action_type"])
            for pi, pr in p.iterrows():
                pa = norm_action(pr["predicted_action_type"])
                dt = float(pr["timestamp_s"] - gr["timestamp_s"])
                if abs(dt) > tolerance_s:
                    continue
                if class_mode == "exact" and ga != pa:
                    continue
                candidates.append((abs(dt), str(gr["event_id"]), str(pr["prediction_id"]), gi, pi, dt))

        candidates.sort(key=lambda z: (z[0], z[1], z[2]))
        used_g, used_p = set(), set()
        matches = []
        for _, _, _, gi, pi, dt in candidates:
            if gi in used_g or pi in used_p:
                continue
            used_g.add(gi)
            used_p.add(pi)
            matches.append((gi, pi, dt))

        for gi, pi, dt in matches:
            gr, pr = g.iloc[gi], p.iloc[pi]
            out = {
                "match_id": match_id,
                "reference_event_id": gr["event_id"],
                "prediction_id": pr["prediction_id"],
                "outcome": "TP",
                "reference_timestamp_s": gr["timestamp_s"],
                "prediction_timestamp_s": pr["timestamp_s"],
                "time_error_s": dt,
                "abs_time_error_s": abs(dt),
                "reference_action_type": norm_action(gr["action_type"]),
                "predicted_action_type": norm_action(pr["predicted_action_type"]),
                "class_correct": norm_action(gr["action_type"]) == norm_action(pr["predicted_action_type"]),
            }
            for c in gt_context:
                if c in g.columns:
                    out[c] = gr[c]
            for c in pred_context:
                if c in p.columns:
                    out[c] = pr[c]
            rows.append(out)

        for gi, gr in g.iterrows():
            if gi in used_g:
                continue
            out = {
                "match_id": match_id,
                "reference_event_id": gr["event_id"],
                "prediction_id": "",
                "outcome": "FN",
                "reference_timestamp_s": gr["timestamp_s"],
                "prediction_timestamp_s": pd.NA,
                "time_error_s": pd.NA,
                "abs_time_error_s": pd.NA,
                "reference_action_type": norm_action(gr["action_type"]),
                "predicted_action_type": "",
                "class_correct": False,
            }
            for c in gt_context:
                if c in g.columns:
                    out[c] = gr[c]
            rows.append(out)

        for pi, pr in p.iterrows():
            if pi in used_p:
                continue
            out = {
                "match_id": match_id,
                "reference_event_id": "",
                "prediction_id": pr["prediction_id"],
                "outcome": "FP",
                "reference_timestamp_s": pd.NA,
                "prediction_timestamp_s": pr["timestamp_s"],
                "time_error_s": pd.NA,
                "abs_time_error_s": pd.NA,
                "reference_action_type": "",
                "predicted_action_type": norm_action(pr["predicted_action_type"]),
                "class_correct": False,
            }
            for c in pred_context:
                if c in p.columns:
                    out[c] = pr[c]
            rows.append(out)

    out = pd.DataFrame(rows)
    if not out.empty:
        out = out.sort_values(
            ["match_id", "reference_timestamp_s", "prediction_timestamp_s"],
            na_position="last",
            kind="stable",
        ).reset_index(drop=True)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ground_truth_csv", type=Path)
    ap.add_argument("predictions_csv", type=Path)
    ap.add_argument("--tolerance-s", type=float, required=True,
                    help="Maximum absolute temporal distance allowed for event matching.")
    ap.add_argument("--class-mode", choices=["exact", "ignore"], default="exact",
                    help="exact: action class must match; ignore: temporal detection only.")
    ap.add_argument("--output", type=Path, default=Path("matched_events.csv"))
    args = ap.parse_args()

    gt = pd.read_csv(args.ground_truth_csv)
    pred = pd.read_csv(args.predictions_csv)
    out = match_events(gt, pred, args.tolerance_s, args.class_mode)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)
    print(f"wrote {len(out)} rows to {args.output}")


if __name__ == "__main__":
    main()
