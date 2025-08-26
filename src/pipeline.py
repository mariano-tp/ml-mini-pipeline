# src/pipeline.py
from __future__ import annotations

import json
from pathlib import Path

import joblib
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split


ARTIFACTS_DIR = Path("artifacts")
MODEL_PATH = ARTIFACTS_DIR / "model.pkl"
METRICS_PATH = ARTIFACTS_DIR / "metrics.json"


def train_and_evaluate(
    n_samples: int = 300,
    n_features: int = 10,
    random_state: int = 42,
) -> tuple[LogisticRegression, dict]:
    """
    Entrena un modelo simple de clasificación y guarda artefactos:
    - model.pkl (modelo entrenado)
    - metrics.json (accuracy, precision, recall, f1)
    """
    # 1) Datos sintéticos
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=6,
        n_redundant=0,
        random_state=random_state,
    )

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=random_state
    )

    # 2) Modelo
    model = LogisticRegression(max_iter=200)
    model.fit(X_tr, y_tr)

    # 3) Métricas
    y_pred = model.predict(X_te)
    metrics = {
        "accuracy": float(accuracy_score(y_te, y_pred)),
        "precision": float(precision_score(y_te, y_pred)),
        "recall": float(recall_score(y_te, y_pred)),
        "f1": float(f1_score(y_te, y_pred)),
    }

    # 4) Guardar artefactos
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    with METRICS_PATH.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    return model, metrics


if __name__ == "__main__":
    train_and_evaluate()
