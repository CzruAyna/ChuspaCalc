# Registro del fallo del sistema CI en la rama `main`

## 1. Datos generales
- Elaborado el: 15 de julio de 2026
- Rama afectada: `main`
- Tarea: Issue #644

## 2. ¿Desde cuándo falla?
- Última revisión completa sin fallos: 16 de junio de 2026, 7:26 p.m.
- Primera revisión fallida: 16 de junio de 2026, 7:26 p.m.
- Causa del inicio: al unir la solicitud de cambios #508
- Estado: **falla continuamente desde esa fecha hasta hoy**

## 3. ¿Por qué ocurre?
Al ejecutar `ruff check` se detecta:
- 27 errores en total
- Error principal `E902`: sintaxis incorrecta en archivos `__init__.py`
- Estos archivos quedaron dañados antes de aplicar correcciones
- El fallo impide verificar si el programa arranca bien, y pasó desapercibido mucho tiempo

## 4. Cómo evitar que pase desapercibido
1. Mostrar el estado del CI en la página principal del proyecto
2. Enviar aviso al equipo si falla más de 24 horas seguidas
3. Revisar obligatoriamente el CI antes de unir cambios a `main`
4. Comprobar semanalmente que las revisiones automáticas funcionen

## 5. Aclaración
Este documento solo describe el fallo; **no modifica ni arregla ningún código**.
