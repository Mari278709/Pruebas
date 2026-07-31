#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "istte.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. Asegúrate de tenerlo instalado en tu entorno virtual. "
            "Puedes instalarlo con 'pip install django'."
        ) from exc
    execute_from_command_line(sys.argv)
