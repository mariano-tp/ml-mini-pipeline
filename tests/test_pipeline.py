from pathlib import Path
from app.train import train


def test_training_produces_artifacts(tmp_path: Path):
    metrics = train(output_dir=tmp_path)
    assert metrics["accuracy"] >= 0.9
    assert (tmp_path / "model.pkl").exists()
    assert (tmp_path / "metrics.json").exists()
