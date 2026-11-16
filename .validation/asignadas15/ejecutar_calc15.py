from importlib import import_module
import os
from pathlib import Path
import sys
from tempfile import mkdtemp

import pytest


root = Path(__file__).resolve().parent
opciones = {
    "1930": ["tests/test_matrix.py"],
    "1923": ["tests/test_csv_parser.py", "tests/test_io.py"],
    "1986": ["tests/modulos/test_resolucion_triangulos.py",
             "tests/modulos/test_herramienta_resolucion_triangulos.py"],
    "1978": ["tests/modulos/test_coordenadas.py"],
}

issue, modo = sys.argv[1:3]
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
sys.path.insert(0, str(Path.cwd() / "src"))
paquete = import_module("escuadra")
print(f"Fuentes evaluadas: {paquete.__file__}", flush=True)
assert Path(paquete.__file__).is_relative_to(Path.cwd() / "src")
sys.modules["chuspacalc"] = paquete
args = ["-q", "--tb=short", "--basetemp", mkdtemp(prefix=f"pytest-{issue}-", dir=root)]
if modo == "auxiliar":
    args += [str(root / "pruebas_calc15.py"), "-k", f"issue{issue}"]
elif modo == "existentes":
    args += opciones[issue]
else:
    raise ValueError(modo)
raise SystemExit(pytest.main(args))
