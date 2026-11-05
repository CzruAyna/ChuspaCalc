# Herramienta de Cálculo de Circuitos RC y RL

Este módulo proporciona la documentación técnica y la base teórica para el cálculo de las constantes de tiempo y el comportamiento transitorio (carga y descarga exponencial) en circuitos eléctricos con resistores, capacitores e inductores.

## 1. Constante de Tiempo (Tau)

La constante de tiempo (denominada tau) representa el tiempo necesario para que la variable de interés (tensión o corriente) alcance aproximadamente el **63.2%** de su cambio total hacia el valor estacionario.

* **Circuitos RC (Resistor-Capacitor):**
  tau = R * C
  Donde **R** es la resistencia en ohmios (Ohm) y **C** es la capacitancia en faradios (F).

* **Circuitos RL (Resistor-Inductor):**
  tau = L / R
  Donde **L** es la inductancia en henrios (H) y **R** es la resistencia en ohmios (Ohm).

---

## 2. Circuitos RC: Carga y Descarga del Capacitor

### Carga Exponencial
Cuando se aplica una fuente de voltaje continua (V0) a un circuito RC inicialmente descargado, el voltaje en el capacitor evoluciona según la función:
V_C(t) = V0 * (1 - e^(-t / tau))

### Descarga Exponencial
Cuando un capacitor cargado con un voltaje inicial (V0) se descarga a través de una resistencia sin fuente externa:
V_C(t) = V0 * e^(-t / tau)

---

## 3. Circuitos RL: Carga y Descarga del Inductor

### Carga Exponencial (Establecimiento de Corriente)
Al conectar una fuente de voltaje constante (V0), la corriente que atraviesa el inductor aumenta gradualmente:
I_L(t) = (V0 / R) * (1 - e^(-t / tau))

### Descarga Exponencial (Decaimiento de Corriente)
Cuando se desconecta la fuente principal y la energía almacenada en el campo magnético del inductor se disipa sobre la resistencia desde una corriente inicial (I0):
I_L(t) = I0 * e^(-t / tau)

---

## 4. Implementación en Python

A continuación, se presenta cómo se modelan estos cálculos utilizando Python dentro de las utilidades del proyecto:

```python
import math

def calcular_tau_rc(resistencia: float, capacitancia: float) -> float:
    """Calcula la constante de tiempo tau para un circuito RC."""
    if resistencia <= 0 or capacitancia <= 0:
        raise ValueError("La resistencia y capacitancia deben ser valores positivos.")
    return resistencia * capacitancia

def calcular_tau_rl(inductancia: float, resistencia: float) -> float:
    """Calcula la constante de tiempo tau para un circuito RL."""
    if inductancia <= 0 or resistencia <= 0:
        raise ValueError("La inductancia y resistencia deben ser valores positivos.")
    return inductancia / resistencia

def voltaje_carga_rc(v0: float, tau: float, t: float) -> float:
    """Calcula el voltaje en el capacitor durante la carga en el instante t."""
    return v0 * (1 - math.exp(-t / tau))

def corriente_carga_rl(v0: float, resistencia: float, tau: float, t: float) -> float:
    """Calcula la corriente en el inductor durante la carga en el instante t."""
    i_max = v0 / resistencia
    return i_max * (1 - math.exp(-t / tau))
