# Proyecto Django ISTTE

Este proyecto contiene una versión Django del portal institucional del Instituto Tecnológico Superior Tecnoecuatoriano.

## Estructura principal

- `manage.py` - script principal de Django.
- `istte/` - configuración del proyecto Django.
- `webapp/` - aplicación que sirve las páginas del sitio.
- `templates/` - plantillas HTML de Django.
- `static/css/custom.css` - estilos personalizados.
- `static/js/main.js` - scripts interactivos.
- `legacy_site/` - copia de los HTML estáticos originales.

## Cómo arrancar

1. Instala Django en el entorno virtual:
   ```bash
   pip install django
   ```
2. Aplica migraciones:
   ```bash
   python manage.py migrate
   ```
3. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```
4. Abre `http://127.0.0.1:8000` en el navegador.

## Observaciones

- Las rutas principales están definidas en `webapp/urls.py`.
- El layout común se maneja en `templates/base.html`.
- El CSS y JS del portal permanecen en `static/`.
