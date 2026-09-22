#!/usr/bin/env python3
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from match_events import match_events
from evaluate_predictions import metrics


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

    loose = match_events(gt, pred, tolerance_s=0.5, class_mode="ignore")
    m2 = metrics(loose)
    assert (m2["TP"], m2["FP"], m2["FN"]) == (2, 1, 0), m2
    assert int((loose["class_correct"] == False).sum()) >= 1

    print("FST SSAC evaluation smoke test passed.")


if __name__ == "__main__":
    main()
