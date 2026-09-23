#!/usr/bin/env python3
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from match_events import match_events
from evaluate_predictions import metrics, risk_coverage, cluster_bootstrap


def main():
    gt = pd.DataFrame([
        {"event_id":"g1","match_id":"m1","timestamp_s":1.0,"action_type":"turning_head_kick"},
        {"event_id":"g2","match_id":"m1","timestamp_s":5.0,"action_type":"non_turning_head_kick"},
    ])
    pred = pd.DataFrame([
        {"prediction_id":"p1","match_id":"m1","timestamp_s":1.1,"predicted_action_type":"turning_head_kick","model_uncertainty":0.1},
        {"prediction_id":"p2","match_id":"m1","timestamp_s":5.2,"predicted_action_type":"turning_head_kick","model_uncertainty":0.3},
        {"prediction_id":"p3","match_id":"m1","timestamp_s":8.0,"predicted_action_type":"turning_head_kick","model_uncertainty":0.8},
    ])

    exact = match_events(gt, pred, tolerance_s=0.5, class_mode="exact")
    m = metrics(exact)
    assert (m["TP"], m["FP"], m["FN"]) == (1, 2, 1), m
    assert abs(m["precision"] - 1/3) < 1e-12
    assert abs(m["recall"] - 1/2) < 1e-12
    assert abs(m["f1"] - 0.4) < 1e-12

    loose = match_events(gt, pred, tolerance_s=0.5, class_mode="ignore")
    m2 = metrics(loose)
    assert (m2["TP"], m2["FP"], m2["FN"]) == (2, 1, 0), m2
    assert int((loose["class_correct"] == False).sum()) >= 1

    selective = pd.DataFrame([
        {"outcome":"TP", "match_id":"m1", "model_uncertainty":0.10},
        {"outcome":"TP", "match_id":"m1", "model_uncertainty":0.20},
        {"outcome":"FP", "match_id":"m2", "model_uncertainty":0.80},
        {"outcome":"FP", "match_id":"m2", "model_uncertainty":0.90},
    ])
    rc = risk_coverage(selective, "model_uncertainty", uncertainty_higher=True, points=4)
    assert not rc.empty
    assert rc.iloc[0]["selective_risk"] == 0.0
    assert abs(rc.iloc[-1]["selective_risk"] - 0.5) < 1e-12
    assert abs(rc.iloc[-1]["coverage"] - 1.0) < 1e-12

    boot = cluster_bootstrap(selective, "match_id", reps=25, seed=2026)
    assert len(boot) == 25
    assert {"precision", "recall", "f1"}.issubset(boot.columns)

    try:
        match_events(gt, pred, tolerance_s=0, class_mode="exact")
    except ValueError:
        pass
    else:
        raise AssertionError("non-positive temporal tolerance must fail")

    print("FST SSAC evaluation smoke test passed.")


if __name__ == "__main__":
    main()
