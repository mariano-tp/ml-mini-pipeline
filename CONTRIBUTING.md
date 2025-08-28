# Guía de Contribución

Gracias por tu interés 🙌. Este repo está pensado para ser simple y reproducible.

## Flujo de trabajo
1. **Abrí un issue** si el cambio afecta el pipeline o métricas.
2. **Creá una rama** desde `main` (`feat/...`, `fix/...`, `docs/...`, `ci/...`).
3. **Commits** estilo *Conventional Commits*.
4. **Pull Request**:
   - Un tema por PR
   - Link al issue
   - Confirmar que los artefactos se generan antes de los tests
   - Pasar todos los checks de CI

## Estilo / calidad
- Código simple y reproducible.
- Documentar cambios en métricas en README.
- Cuidar reproducibilidad (semilla fija).

## CI
Los PRs deben quedar en **verde**:
- Ejecutar pipeline (artefactos en `artifacts/`)
- `pytest -q`

## Licencia
Al contribuir aceptás que tu aporte se publica bajo **MIT** (ver `LICENSE`).
