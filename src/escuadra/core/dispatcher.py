"""
Despachador de comandos que mapea subcomandos a funciones ejecutables
consultando dinámicamente al registry.
"""

import sys

from . import registry


def _cargar_modulos_dinamicos() -> None:
    """Carga dinámicamente los módulos de la carpeta 'modulos'."""
    registry.descubrir_herramientas()


def dispatch(subcommand: str) -> int:
    """
    Despacha un subcomando a su función ejecutable correspondiente.

    Args:
        subcommand: Nombre del subcomando a ejecutar.

    Returns:
        Código de salida entero (0 para éxito).

    Examples:
        >>> dispatch("convert")
        Ejecutando conversión...
        0
        >>> dispatch("desconocido")
        Error: subcomando desconocido 'desconocido'
        1
    """
    # Forzamos el descubrimiento automático de submódulos antes de consultar
    _cargar_modulos_dinamicos()

    try:
        herramienta = registry.buscar_por_nombre(subcommand)
        if herramienta is None:
            print(f"Error: subcomando desconocido '{subcommand}'", file=sys.stderr)
            return 1
        instancia = herramienta()
        ejecutar = getattr(instancia, "ejecutar", None)
        if not callable(ejecutar):
            print("Error: la herramienta no ofrece ejecucion por consola.", file=sys.stderr)
            return 1
        codigo = ejecutar()
        return 0 if codigo is None else int(codigo)
    except (ImportError, ModuleNotFoundError):
        print("Error: El modulo solicitado no esta disponible o no existe.", file=sys.stderr)
        return 1
