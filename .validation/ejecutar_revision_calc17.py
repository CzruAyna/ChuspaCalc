from importlib import import_module
from pathlib import Path
import argparse
import ast
import os
import sys
from tempfile import mkdtemp

parser=argparse.ArgumentParser()
parser.add_argument("--issue",choices=["1930","1923","1986","1978"])
parser.add_argument("--repo",type=Path,default=Path.cwd())
parser.add_argument("--completo",action="store_true")
parser.add_argument("--junit",type=Path)
args=parser.parse_args()
raiz=Path(__file__).resolve().parent
repo=args.repo.resolve()
os.environ.setdefault("QT_QPA_PLATFORM","offscreen")
sys.path.insert(0,str(repo/"src"))
paquete=import_module("chuspacalc")
print(f"Fuentes evaluadas: {paquete.__file__}",flush=True)
assert Path(paquete.__file__).resolve().is_relative_to(repo/"src")
os.chdir(repo)
import pytest

rutas={
"1930":["tests/test_matrix.py"],
"1923":["tests/test_csv_parser.py","tests/test_io.py"],
"1986":["tests/modulos/test_resolucion_triangulos.py","tests/modulos/test_herramienta_resolucion_triangulos.py"],
"1978":["tests/modulos/test_coordenadas.py"],
}
opciones=["-q","--tb=short","--basetemp",mkdtemp(prefix="calc-revision17-pytest-",dir=raiz)]
if args.junit:
    opciones+=["--junitxml",str(args.junit.resolve())]
if args.completo:
    opciones+=["-m","not slow","tests"]
else:
    assert args.issue
    pruebas=raiz/"pruebas_revision_calc17.py"
    nodos=ast.parse(pruebas.read_text(encoding="utf-8")).body
    nombres=[n.name for n in nodos if isinstance(n,ast.FunctionDef) and n.name.startswith(f"test_issue{args.issue}_")]
    opciones+=rutas[args.issue]+[str(pruebas)+"::"+n for n in nombres]
raise SystemExit(pytest.main(opciones))
