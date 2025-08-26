from __future__ import annotations
from pathlib import Path
from joblib import load
from src.train import train_and_save
import numpy as np

def test_training_produces_artifacts():
    metrics = train_and_save()
    assert metrics["accuracy"] > 0.8

    assert (Path("artifacts") / "model.pkl").exists()
    assert (Path("artifacts") / "metrics.json").exists()

def test_model_predict_shape():
    train_and_save()
    model = load(Path("artifacts") / "model.pkl")
    out = model.predict(np.zeros((5, 3), dtype="float32"))
    assert out.shape == (5,)
