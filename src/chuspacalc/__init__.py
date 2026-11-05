import sys
from importlib import import_module
from pathlib import Path

from escuadra import __version__ as __version__

__path__.append(str(Path(__file__).resolve().parent.parent / "escuadra"))
_paquete_core = import_module(f"{__name__}.core")
for _nombre_modulo in ("carrera", "herramienta"):
    _modulo_real = import_module(f"escuadra.core.{_nombre_modulo}")
    sys.modules[f"{__name__}.core.{_nombre_modulo}"] = _modulo_real
    setattr(_paquete_core, _nombre_modulo, _modulo_real)
