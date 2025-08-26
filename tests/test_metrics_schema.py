import json
from pathlib import Path


def test_metrics_schema_exists_and_has_keys():
    m = Path("artifacts") / "metrics.json"
    assert m.exists(), "No se encontró artifacts/metrics.json (la pipeline debe generarlo)"

    data = json.loads(m.read_text())

    # Debe existir al menos una de estas llaves, preferentemente todas:
    keys = {"accuracy", "f1", "rmse"}
    assert keys & data.keys(), f"Faltan llaves esperadas en metrics.json, esperadas: {keys}"
