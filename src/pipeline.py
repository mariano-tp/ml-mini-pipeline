from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any, Dict, List


ARTIFACTS_DIR = Path("artifacts")
METRICS_FILE = ARTIFACTS_DIR / "metrics.json"
PREDICTIONS_FILE = ARTIFACTS_DIR / "predictions.csv"


def ensure_dirs() -> None:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


def train_dummy_model(seed: int = 42) -> Dict[str, Any]:
    """
    Simula el entrenamiento y devuelve métricas simples.
    """
    random.seed(seed)
    # Métricas simuladas pero razonables
    accuracy = round(random.uniform(0.80, 0.98), 4)
    f1 = round(random.uniform(0.78, 0.97), 4)
    rmse = round(random.uniform(0.10, 0.30), 4)
    return {"accuracy": accuracy, "f1": f1, "rmse": rmse}


def generate_predictions(n: int = 10, seed: int = 123) -> List[float]:
    random.seed(seed)
    return [round(random.uniform(0, 1), 4) for _ in range(n)]


def save_metrics(metrics: Dict[str, Any]) -> None:
    METRICS_FILE.write_text(json.dumps(metrics, indent=2))


def save_predictions(preds: List[float]) -> None:
    lines = ["prediction"]
    lines += [str(p) for p in preds]
    PREDICTIONS_FILE.write_text("\n".join(lines))


def main() -> None:
    ensure_dirs()
    metrics = train_dummy_model()
    preds = generate_predictions()

    save_metrics(metrics)
    save_predictions(preds)

    print(f"[pipeline] Métricas -> {METRICS_FILE}")
    print(f"[pipeline] Predicciones -> {PREDICTIONS_FILE}")


if __name__ == "__main__":
    main()
