[![CI](https://img.shields.io/github/actions/workflow/status/mariano-tp/ml-mini-pipeline/ci.yml?branch=main&label=tests&style=flat-square)](./.github/workflows/ci.yml)
[![release](https://img.shields.io/github/v/release/mariano-tp/ml-mini-pipeline?display_name=tag&style=flat-square)](../../releases)
[![license: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)

# ml-mini-pipeline

Mini pipeline de ML con **scikit-learn**:
- genera dataset sintético,
- entrena un modelo (LogisticRegression),
- guarda artefactos (`model.pkl`, `metrics.json`) y
- corre **pytest** en CI.

> 100% online: solo subí el repo y ejecutá **Actions**.

## Ejecutar local (opcional)
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/train.py
python src/predict.py --x 0.5 --y -1.2 --z 0.1
pytest -q
```

## Estructura
```
.
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── train.py
│   └── predict.py
├── tests/test_pipeline.py
├── requirements.txt
├── .github/workflows/ci.yml
└── LICENSE
```

## CI
- Instala dependencias
- `python src/train.py` (genera artefactos en `artifacts/`)
- `pytest -q`
- Publica `artifacts/` como artifact del run

## Créditos
Repositorio de portfolio por @mariano-tp. Licencia MIT.

Ver también: [Código de Conducta](./CODE_OF_CONDUCT.md) · [Contribuir](./CONTRIBUTING.md) · [Seguridad](./SECURITY.md)
