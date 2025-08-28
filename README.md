[![ci](https://img.shields.io/github/actions/workflow/status/mariano-tp/ml-mini-pipeline/ci.yml?branch=main&label=tests&style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/actions/workflows/ci.yml)
[![model-ci](https://img.shields.io/github/actions/workflow/status/mariano-tp/ml-mini-pipeline/model-ci.yml?branch=main&label=model-ci&style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/actions/workflows/model-ci.yml)
[![last commit](https://img.shields.io/github/last-commit/mariano-tp/ml-mini-pipeline?style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/commits/main)
[![release](https://img.shields.io/github/v/release/mariano-tp/ml-mini-pipeline?display_name=tag&style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/releases)
[![license: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![stars](https://img.shields.io/github/stars/mariano-tp/ml-mini-pipeline?style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/stargazers)

# Machine Learning (ML) Mini Pipeline

Mini pipeline de Machine Learning (ML) con `scikit-learn` pensada para portfolio:
- genera un dataset sintético,
- entrena un modelo (`LogisticRegression`),
- guarda artefactos en `./artifacts/` (`model.pkl` y `metrics.json`),
- corre **pytest** en CI con **GitHub Actions**.

> 100% online: subí el repo y ejecutá **Actions**; el pipeline se entrena en CI y publica artefactos del run.

---

## Ejecutar local (opcional)

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt -r requirements-dev.txt

# entrenar y guardar artefactos
python -c "from src.pipeline import train_and_evaluate; train_and_evaluate()"

# tests
pytest -q
```

### Artefactos generados

```
artifacts/
├── model.pkl
└── metrics.json
```

`metrics.json` (ejemplo):

```json
{
  "accuracy": 0.89,
  "precision": 0.88,
  "recall": 0.91,
  "f1": 0.89,
  "timestamp": "2025-08-24T18:00:00Z",
  "model_type": "LogisticRegression"
}
```

---

## CI (GitHub Actions)

El workflow `ci.yml` ejecuta en cada *push/PR*:
1) Instalación de dependencias.
2) **Entrenamiento** del modelo (genera `artifacts/`).
3) **Tests** con `pytest`.
4) (Opcional) Publicación de artefactos del run.

Para subir artefactos, agregá este paso al final del job:

```yaml
- name: Upload artifacts (model + metrics)
  uses: actions/upload-artifact@v4
  with:
    name: artifacts
    path: artifacts/**
```

---

## Estructura

```text
.
├── artifacts/               # generado por la pipeline (ignorado por git)
├── src/
│   ├── __init__.py
│   └── pipeline.py          # orquestación (train_and_evaluate)
├── tests/
│   ├── test_metrics_schema.py
│   └── test_pipeline.py
├── requirements.txt
├── requirements-dev.txt
└── .github/workflows/ci.yml
```

---

## Releases

- Crear una versión desde **Releases → Draft new release** (ej. `v0.1.0`).
- Etiquetar como *Latest* y pinnear para que se vea en el README (badge de release).

---

## Créditos

Repositorio de portfolio por **@mariano-tp**. Inspirado en prácticas de MLOps minimalistas (datos sintéticos + artefactos + CI).

Ver también: [Código de Conducta](./CODE_OF_CONDUCT.md) · [Contribuir](./CONTRIBUTING.md) · [Seguridad](./SECURITY.md)
