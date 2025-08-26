from __future__ import annotations
import argparse
from pathlib import Path
from joblib import load
import numpy as np

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--x", type=float, required=True)
    p.add_argument("--y", type=float, required=True)
    p.add_argument("--z", type=float, required=True)
    args = p.parse_args()

    model = load(Path("artifacts") / "model.pkl")
    X = np.array([[args.x, args.y, args.z]], dtype="float32")
    proba = model.predict_proba(X)[0].tolist()
    print({"proba": proba})

if __name__ == "__main__":
    main()
