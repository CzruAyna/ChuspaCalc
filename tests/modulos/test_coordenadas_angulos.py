import math

import pytest

from chuspacalc.modulos.geometria import coordenadas


@pytest.mark.parametrize("x,y,angulo", [(1, 1, 45), (-1, 1, 135), (-1, -1, 225), (1, -1, 315)])
def test_coordenadas_polares_cuadrantes(x, y, angulo):
    resultado = coordenadas.cartesiana_a_polar(x, y)
    assert resultado["r"] == pytest.approx(math.sqrt(2))
    assert resultado["theta_grados"] == angulo
    assert resultado["theta_radianes"] == pytest.approx(math.radians(angulo))


@pytest.mark.parametrize("x,y,z,elevacion", [(0, 0, 1, 90), (0, 0, -1, -90), (1, 0, 0, 0)])
def test_coordenadas_elevacion(x, y, z, elevacion):
    resultado = coordenadas.cartesiana_a_esferica(x, y, z)
    assert resultado["rho"] == 1
    assert resultado["elevacion_grados"] == pytest.approx(elevacion)
    assert resultado["elevacion_radianes"] == pytest.approx(math.radians(elevacion))


def test_coordenadas_origen():
    polar = coordenadas.cartesiana_a_polar(0, 0)
    esfera = coordenadas.cartesiana_a_esferica(0, 0, 0)
    assert all(valor == 0 for valor in polar.values())
    assert all(valor == 0 for valor in esfera.values())


def test_coordenadas_reconstruye_tridimensional():
    x, y, z = -2, 3, -4
    resultado = coordenadas.cartesiana_a_esferica(x, y, z)
    radio = resultado["rho"]
    azimut = resultado["theta_radianes"]
    elevacion = resultado["elevacion_radianes"]
    assert radio * math.cos(elevacion) * math.cos(azimut) == pytest.approx(x)
    assert radio * math.cos(elevacion) * math.sin(azimut) == pytest.approx(y)
    assert radio * math.sin(elevacion) == pytest.approx(z)
    assert resultado["phi_grados"] == round(90 - resultado["elevacion_grados"], 2)


@pytest.mark.parametrize("valor", [1e300, 1e-300])
def test_coordenadas_magnitudes_extremas(valor):
    resultado = coordenadas.cartesiana_a_esferica(valor, valor, valor)
    assert math.isfinite(resultado["rho"])
    assert resultado["rho"] > 0
    assert resultado["elevacion_grados"] == pytest.approx(math.degrees(math.atan(1 / math.sqrt(2))))
