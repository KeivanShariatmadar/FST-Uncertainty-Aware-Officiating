#!/usr/bin/env python3
"""Fail-fast validation for FST SSAC derived evaluation tables."""
import argparse
from pathlib import Path
import pandas as pd

REQUIRED = {
 "ground_truth_events.csv": ["event_id", "match_id"],
 "fst_ssac_predictions.csv": ["prediction_id", "match_id"],
 "matched_events.csv": ["match_id", "outcome"],
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("directory", type=Path)
    args = ap.parse_args()
    errors=[]
    for name, cols in REQUIRED.items():
        p=args.directory/name
        if not p.exists():
            errors.append(f"missing: {name}"); continue
        df=pd.read_csv(p)
        miss=[c for c in cols if c not in df.columns]
        if miss: errors.append(f"{name}: missing columns {miss}")
        if name=="ground_truth_events.csv" and "event_id" in df and df.event_id.duplicated().any():
            errors.append("ground_truth_events.csv: duplicate event_id")
        if name=="fst_ssac_predictions.csv" and "prediction_id" in df and df.prediction_id.duplicated().any():
            errors.append("fst_ssac_predictions.csv: duplicate prediction_id")
        if name=="matched_events.csv" and "outcome" in df:
            bad=sorted(set(df.outcome.dropna().astype(str).str.upper())-{"TP","FP","FN","TN"})
            if bad: errors.append(f"matched_events.csv: invalid outcomes {bad}")
    if errors:
        print("VALIDATION FAILED")
        for e in errors: print("-",e)
        raise SystemExit(1)
    print("VALIDATION PASSED")

if __name__=="__main__": main()
