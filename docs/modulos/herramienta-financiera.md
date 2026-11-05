# Módulo de Herramienta Financiera

Este módulo proporciona funciones para realizar cálculos financieros fundamentales, integrados en el sistema para facilitar la toma de decisiones financieras.

## Descripción de Funciones

A continuación, se describen las funciones disponibles para el cálculo de interés compuesto, valor presente y valor futuro.

### 1. Interés Compuesto
Calcula el monto final generado a partir de un capital inicial, considerando una tasa de interés periódica y un número de periodos de capitalización.

- **Fórmula:** M = C * (1 + i)^n
- **Uso:** Ideal para determinar el crecimiento de inversiones a largo plazo.

### 2. Valor Presente (VP)
Determina el valor actual de un monto de dinero que se recibirá o pagará en el futuro, descontando una tasa de interés específica.

- **Fórmula:** VP = VF / (1 + i)^n
- **Uso:** Permite comparar flujos de dinero en diferentes momentos del tiempo, trayéndolos a valor de hoy.

### 3. Valor Futuro (VF)
Calcula el valor equivalente en una fecha futura de un capital disponible hoy, aplicando una tasa de interés compuesta.

- **Fórmula:** VF = VP * (1 + i)^n
- **Uso:** Útil para proyecciones de ahorro o crecimiento de capital.

---
*Nota: Asegúrese de que la tasa de interés (i) se proporcione en formato decimal (por ejemplo, 0.05 para 5%) y que el número de periodos (n) coincida con la frecuencia de la tasa.*
