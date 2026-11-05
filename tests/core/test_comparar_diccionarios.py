import math

import pytest

from chuspacalc.core import comparar


def test_comparar_porcentaje_y_claves():
    a = {"carga": 200, "temperatura": -20, "nombre": "A", "solo_a": 1}
    b = {"carga": 250, "temperatura": -10, "nombre": "A", "solo_b": 2}
    resultado = comparar.comparar_diccionarios_resultados(a, b)
    assert set(resultado) == {"diferencias_numericas", "coincidentes", "claves_disjuntas"}
    assert resultado["diferencias_numericas"]["carga"]["diferencia_absoluta"] == 50
    assert resultado["diferencias_numericas"]["carga"]["diferencia_porcentual"] == 25
    assert resultado["diferencias_numericas"]["temperatura"]["diferencia_porcentual"] == 50
    assert resultado["coincidentes"] == ["nombre"]
    assert resultado["claves_disjuntas"] == {"solo_a": ["solo_a"], "solo_b": ["solo_b"]}
    assert a["carga"] == 200 and b["carga"] == 250


@pytest.mark.parametrize("destino,porcentaje", [(0, 0), (2, None), (-2, None)])
def test_comparar_base_cero(destino, porcentaje):
    resultado = comparar.comparar_diccionarios_resultados({"a": 0}, {"a": destino})
    assert resultado["diferencias_numericas"]["a"]["diferencia_porcentual"] == porcentaje


def test_comparar_tolerancia_y_datos_no_numericos():
    resultado = comparar.comparar_diccionarios_resultados(
        {"cerca": 1, "lejos": 1, "booleano": True, "lista": [1, 2]},
        {"cerca": 1.00001, "lejos": 1.1, "booleano": 1, "lista": [1, 2]},
    )
    assert resultado["coincidentes"] == ["cerca", "lista"]
    assert "booleano" not in resultado["diferencias_numericas"]


def test_comparar_vacios_y_tolerancia_exacta():
    assert comparar.comparar_diccionarios_resultados({}, {}) == {
        "diferencias_numericas": {},
        "coincidentes": [],
        "claves_disjuntas": {"solo_a": [], "solo_b": []},
    }
    assert comparar.comparar_diccionarios_resultados({"a": 1}, {"a": 1}, 0)["coincidentes"] == ["a"]


@pytest.mark.parametrize("tolerancia", [-1, None, True, "0.1", math.nan, math.inf])
def test_comparar_rechaza_tolerancia_invalida(tolerancia):
    with pytest.raises(ValueError):
        comparar.comparar_diccionarios_resultados({}, {}, tolerancia)


@pytest.mark.parametrize("a,b", [(None, {}), ({}, []), (1, {})])
def test_comparar_rechaza_entradas(a, b):
    with pytest.raises(TypeError):
        comparar.comparar_diccionarios_resultados(a, b)


@pytest.mark.parametrize("valor", [math.nan, math.inf, -math.inf])
def test_comparar_rechaza_no_finitos(valor):
    with pytest.raises(ValueError):
        comparar.comparar_diccionarios_resultados({"a": valor}, {"a": 1})


def test_comparar_funcion_anterior_conservada():
    assert comparar.comparar_resultados(1, 1.0000001)["equivalente"] is True
    with pytest.raises(ValueError):
        comparar.comparar_resultados(1, 2, -1)
