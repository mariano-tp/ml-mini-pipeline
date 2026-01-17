> Available languages / Idiomas disponibles: [*English*](README.md) / [*Español*](README.ES.md)

[![ci](https://img.shields.io/github/actions/workflow/status/mariano-tp/ml-mini-pipeline/ci.yml?branch=main&label=tests&style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/actions/workflows/ci.yml)
[![model-ci](https://img.shields.io/github/actions/workflow/status/mariano-tp/ml-mini-pipeline/model-ci.yml?branch=main&label=model-ci&style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/actions/workflows/model-ci.yml)
[![last commit](https://img.shields.io/github/last-commit/mariano-tp/ml-mini-pipeline?style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/commits/main)
[![release](https://img.shields.io/github/v/release/mariano-tp/ml-mini-pipeline?display_name=tag&style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/releases)
[![license: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![stars](https://img.shields.io/github/stars/mariano-tp/ml-mini-pipeline?style=flat-square)](https://github.com/mariano-tp/ml-mini-pipeline/stargazers)

# Machine Learning Mini Pipeline

Pipeline mínima de Machine Learning construida con scikit-learn para portfolio.

Genera datos sintéticos, entrena un modelo LogisticRegression, produce artefactos (modelo + métricas) y valida todo con GitHub Actions.

## Qué hace
- Genera un dataset sintético
- Entrena un modelo (LogisticRegression)
- Escribe artefactos del run en ./artifacts/
  - model.pkl
  - metrics.json
- Corre pytest en CI para validar el pipeline y el esquema de métricas

## Validación 100% online (GitHub Actions)
No hace falta ejecutar nada en local para evaluar este repo.

1. Subí este repo a GitHub
2. Entrá a Actions -> tests (ci.yml) -> Run workflow
3. Entrá a Actions -> model-ci (model-ci.yml) -> Run workflow (opcional)
4. Ambos workflows deberían quedar en verde

Evidencia: logs de Actions y artifacts descargables (si están habilitados).

## Artefactos generados
    artifacts/
    ├── model.pkl
    └── metrics.json

Ejemplo de metrics.json:

    {
      "accuracy": 0.89,
      "precision": 0.88,
      "recall": 0.91,
      "f1": 0.89,
      "timestamp": "2025-08-24T18:00:00Z",
      "model_type": "LogisticRegression"
    }

## CI (GitHub Actions)
- ci.yml (tests)
  - Instala dependencias
  - Ejecuta pytest (tests unitarios)
  - Valida controles básicos de calidad del pipeline

- model-ci.yml (entrenamiento)
  - Entrena el modelo en CI
  - Genera artifacts (model.pkl + metrics.json)
  - Opcionalmente sube artifacts desde el workflow

Si querés publicar artifacts desde CI, agregá este step al final del job del workflow:

    - name: Upload artifacts (model + metrics)
      uses: actions/upload-artifact@v4
      with:
        name: artifacts
        path: artifacts/**

## Ejecución local (opcional)
La ejecución local es opcional y sirve principalmente para desarrollo.

    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt -r requirements-dev.txt

    python -c "from src.pipeline import train_and_evaluate; train_and_evaluate()"
    pytest -q

## Estructura
    .
    ├── artifacts/               # generado por el pipeline (gitignored)
    ├── src/
    │   ├── __init__.py
    │   └── pipeline.py          # orquestación (train_and_evaluate)
    ├── tests/
    │   ├── test_metrics_schema.py
    │   └── test_pipeline.py
    ├── requirements.txt
    ├── requirements-dev.txt
    └── .github/workflows/
        ├── ci.yml
        └── model-ci.yml

## Releases
Creá un release desde Releases -> Draft new release (por ejemplo v0.1.0).
Marcá el tag como Latest para que quede visible en el encabezado del repositorio.

## Créditos
Repositorio de portfolio por @mariano-tp. Inspirado en prácticas MLOps minimalistas (datos sintéticos + artifacts + CI).

Ver también: [Code of Conduct](./CODE_OF_CONDUCT.md) · [Contributing](./CONTRIBUTING.md) · [Security](./SECURITY.md)
