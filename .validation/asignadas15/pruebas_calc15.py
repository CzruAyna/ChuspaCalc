import math
import sys

import pytest

from escuadra.io.csv_parser import parse_csv
from escuadra.math import matrix
from escuadra.modulos.geometria import coordenadas as coords
from escuadra.modulos.geometria import resolucion_triangulos as triangulos
from escuadra.modulos.matematicas.error_validacion import ErrorValidacion


@pytest.mark.parametrize(
    "entrada",
    [None, "", [], [None], [[]], [[1, 2], [3]], [[None]], [[True]], [[math.nan]], [[math.inf]]],
)
def test_issue1930_rechaza_matriz_invalida(entrada):
    for operacion in (matrix.sumar, matrix.restar, matrix.multiplicar):
        with pytest.raises(ValueError):
            operacion(entrada, [[1]])
        with pytest.raises(ValueError):
            operacion([[1]], entrada)
    with pytest.raises(ValueError):
        matrix.transponer(entrada)
    with pytest.raises(ValueError):
        matrix.multiplicar_escalar(entrada, 2)


@pytest.mark.parametrize("escalar", [None, "2", True, math.nan, math.inf])
def test_issue1930_rechaza_escalar_invalido(escalar):
    with pytest.raises(ValueError, match="escalar"):
        matrix.multiplicar_escalar([[1]], escalar)


def test_issue1930_acepta_tuplas_y_no_muta_entradas():
    origen = [[1, 2, 3], [4, 5, 6]]
    assert matrix.transponer(origen) == [[1, 4], [2, 5], [3, 6]]
    assert matrix.sumar(((1, 2),), ((3, 4),)) == [[4, 6]]
    assert matrix.multiplicar_escalar(origen, -2.5) == [
        [-2.5, -5.0, -7.5], [-10.0, -12.5, -15.0]
    ]
    assert origen == [[1, 2, 3], [4, 5, 6]]
    assert matrix.multiplicar_escalar([[10**500]], 2) == [[2 * 10**500]]


@pytest.mark.parametrize(
    "opciones, error",
    [
        ({"file_path": None}, TypeError),
        ({"file_path": 0}, TypeError),
        ({"has_header": "false"}, TypeError),
        ({"delimiter": ";;"}, ValueError),
        ({"delimiter": "\n"}, ValueError),
        ({"encoding": None}, TypeError),
        ({"encoding": ""}, ValueError),
        ({"encoding": "codificacion-desconocida"}, LookupError),
    ],
)
def test_issue1923_valida_opciones(tmp_path, opciones, error):
    ruta = tmp_path / "entrada.csv"
    ruta.write_text("a,b\n1,2\n", encoding="utf-8")
    with pytest.raises(error):
        parse_csv(**({"file_path": ruta} | opciones))


@pytest.mark.parametrize("has_header", [True, False])
def test_issue1923_reporta_comillas_sin_cerrar(tmp_path, has_header):
    ruta = tmp_path / "malformado.csv"
    ruta.write_bytes(b'a,b\n1,"sin cerrar')
    with pytest.raises(ValueError, match="Fila 2: CSV inválido"):
        parse_csv(ruta, has_header=has_header)


def test_issue1923_conserva_lineas_de_celda_y_latino(tmp_path):
    ruta = tmp_path / "normal.csv"
    ruta.write_bytes('a,b\r\n"Peña\r\nalta",2\r\n'.encode("latin-1"))
    assert parse_csv(ruta) == [{"a": "Peña\r\nalta", "b": "2"}]


@pytest.mark.parametrize("valor", [None, True, "1", math.nan, math.inf, 10**500])
def test_issue1986_rechaza_datos_invalidos(valor):
    with pytest.raises(ErrorValidacion, match="a "):
        triangulos.resolver_triangulo_lados(valor, 4, 5)
    with pytest.raises(ErrorValidacion, match="angulo_b "):
        triangulos.resolver_triangulo_lado_angulo(10, 30, valor)


@pytest.mark.parametrize("escala", [1e-200, 1.0, 1e200])
def test_issue1986_angulos_independientes_de_la_escala(escala):
    angulos = triangulos.resolver_triangulo_lados(3 * escala, 4 * escala, 5 * escala)
    assert angulos == pytest.approx((36.8698976458, 53.1301023542, 90.0))


@pytest.mark.parametrize("lados", [(0, 1, 1), (1, 2, 3), (1, 3, 8)])
def test_issue1986_rechaza_triangulos_invalidos(lados):
    with pytest.raises(ErrorValidacion):
        triangulos.resolver_triangulo_lados(*lados)


def test_issue1986_valida_limites_de_la_ley_de_senos():
    assert triangulos.resolver_triangulo_lado_angulo(10, 30, 60) == pytest.approx(
        (10 * math.sqrt(3), 20, 90)
    )
    for datos in [(10, 100, 80), (10, 5e-324, 70), (sys.float_info.max, 30, 60)]:
        with pytest.raises(ErrorValidacion):
            triangulos.resolver_triangulo_lado_angulo(*datos)


@pytest.mark.parametrize("valor", [None, True, "1", math.nan, math.inf, 10**500])
def test_issue1978_rechaza_coordenadas_invalidas(valor):
    with pytest.raises(ErrorValidacion, match="x "):
        coords.cartesiana_a_polar(valor, 4)
    with pytest.raises(ErrorValidacion, match="theta_grados "):
        coords.polar_a_cartesiana(4, valor)
    with pytest.raises(ErrorValidacion, match="z "):
        coords.cartesiana_a_cilindrica(3, 4, valor)
    with pytest.raises(ErrorValidacion, match="z "):
        coords.cartesiana_a_esferica(3, 4, valor)


def test_issue1978_rechaza_radio_negativo_o_desbordado():
    with pytest.raises(ErrorValidacion, match="r debe"):
        coords.polar_a_cartesiana(-1, 90)
    with pytest.raises(ErrorValidacion, match="radio excede"):
        coords.cartesiana_a_esferica(sys.float_info.max, 0, sys.float_info.max)


def test_issue1978_conserva_claves_y_coordenadas():
    assert coords.cartesiana_a_polar(0, 0) == {
        "r": 0.0, "theta_grados": 0.0, "theta_radianes": 0.0,
    }
    assert coords.polar_a_cartesiana(5, 450) == {"x": 0.0, "y": 5.0}
    assert coords.cartesiana_a_cilindrica(3, 4, -7) == {
        "r": 5.0, "theta_grados": 53.13, "z": -7.0,
    }
    assert coords.cartesiana_a_esferica(0, 0, 5) == {
        "rho": 5.0, "theta_grados": 0.0, "theta_radianes": 0.0,
        "phi_grados": 0.0, "phi_radianes": 0.0, "elevacion_grados": 90.0,
        "elevacion_radianes": math.pi / 2,
    }
