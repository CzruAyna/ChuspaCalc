# Validacion del CI

El workflow Python CI comprueba Black, Ruff, pruebas con cobertura y mypy. Los errores en cualquiera de estas etapas mantienen el CI en rojo.

## Entorno

```powershell
python -m pip install -e .
python -m pip install -r requirements-dev.txt
```

En Linux se necesitan tambien las bibliotecas de Qt instaladas por el workflow:

```bash
sudo apt-get update
sudo apt-get install -y libegl1 libopengl0 libxkbcommon0 libxcb-cursor0
export QT_QPA_PLATFORM=offscreen
```

Black, Ruff y mypy usan las mismas versiones en CI y pre-commit. Black y Ruff Format comparten el limite de 100 caracteres.

## Comprobaciones reales

```bash
python -m black --check src/ tests/
python -m ruff check .
python -m pytest -m "not slow" --cov=src/escuadra --cov-report=term-missing
python -m mypy src/escuadra src/chuspacalc
python -m pre_commit run --all-files
```

Las cinco marcas xfail existentes se conservan; no se agregan exclusiones para ocultar errores. Pytest informa por separado los casos aprobados y los fallos esperados.

## Compatibilidad durante la migracion

Las fuentes siguen en src/escuadra porque las issues activas nombran esas rutas. El paquete chuspacalc usa esas mismas fuentes mediante su ruta de busqueda. Carrera y Herramienta conservan una sola identidad entre ambos nombres para que los metadatos, los enums y el descubrimiento de herramientas sean coherentes.

El paquete no contiene implementaciones alternativas de las funciones. Los tests se ejecutan contra el codigo real.

## Comparacion y coordenadas

La prueba de coordenadas conserva las comprobaciones de rho, theta_grados y phi_grados sin exigir que el diccionario contenga exclusivamente esas tres claves. Los campos adicionales se verifican en las pruebas especificas de la funcionalidad de coordenadas.

La reparacion de infraestructura debe integrarse antes de revalidar los PR de funcionalidades. Las pruebas de nuevas funcionalidades se integran despues de sus implementaciones, sin introducir dependencias circulares.
