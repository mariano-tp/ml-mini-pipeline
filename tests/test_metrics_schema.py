import json
from pathlib import Path

def test_metrics_schema_exists_and_has_keys():
    m = Path("artifacts") / "metrics.json"
    assert m.exists(), "No se encontró artifacts/metrics.json (ejecutá la pipeline en CI)"

    data = json.loads(m.read_text())
    # Ajustá las claves si tu pipeline escribe otras métricas
    assert "accuracy" in data or "f1" in data, "metrics.json no contiene métricas esperadas"
