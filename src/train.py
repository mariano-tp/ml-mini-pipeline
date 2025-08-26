from __future__ import annotations
import json
from pathlib import Path
from joblib import dump
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from src.data import make_dataset

ARTIF_DIR = Path("artifacts")
ARTIF_DIR.mkdir(exist_ok=True)

def train_and_save() -> dict:
    ds = make_dataset()
    clf = LogisticRegression(max_iter=300)
    clf.fit(ds.X, ds.y)

    acc = accuracy_score(ds.y, clf.predict(ds.X))
    metrics = {"accuracy": float(acc)}

    dump(clf, ARTIF_DIR / "model.pkl")
    (ARTIF_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2))

    return metrics

if __name__ == "__main__":
    m = train_and_save()
    print("metrics:", m)
