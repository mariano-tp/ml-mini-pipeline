from __future__ import annotations
import json
import os
from pathlib import Path

import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def train(output_dir: str | os.PathLike = "artifacts") -> dict:
    """
    Entrena un modelo simple (Iris) y guarda:
      - artifacts/model.pkl
      - artifacts/metrics.json
    Devuelve un dict con métricas.
    """
    rng = 42
    X, y = load_iris(return_X_y=True, as_frame=False)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=rng, stratify=y
    )

    pipe = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=200, random_state=rng)),
        ]
    )

    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    acc = float(accuracy_score(y_test, preds))

    metrics = {"accuracy": acc, "n_train": int(len(X_train)), "n_test": int(len(X_test))}

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    joblib.dump(pipe, out / "model.pkl")
    with open(out / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    return metrics


if __name__ == "__main__":
    m = train()
    print(json.dumps(m, indent=2))
