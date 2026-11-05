import importlib

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta


def test_carrera_tiene_identidad_unica_entre_paquetes():
    legado = importlib.import_module("escuadra.core.carrera")
    assert Carrera is legado.Carrera
    assert Carrera.CIVIL is legado.Carrera.CIVIL


def test_herramienta_tiene_identidad_unica_entre_paquetes():
    legado = importlib.import_module("escuadra.core.herramienta")
    assert Herramienta is legado.Herramienta


def test_modulo_numerico_canonico_usa_las_fuentes_reales():
    modulo = importlib.import_module("chuspacalc.modulos.geometria.coordenadas")
    assert modulo.cartesiana_a_polar(3, 4)["r"] == 5
    assert "escuadra" in modulo.__file__
