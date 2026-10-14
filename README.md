# Proyecto Django ISTTE

Este proyecto contiene la versión Django del portal institucional del Instituto Tecnológico Superior Tecnoecuatoriano.

Está preparado para ejecutarse **en cualquier computadora (Windows, macOS o Linux)** de forma automática y portátil.

---

## 🚀 Cómo Ejecutar en Cualquier PC

1. Instala las dependencias en el mismo entorno de Python que usarás para ejecutar el servidor:
   ```bash
   pip install -r requirements.txt
   ```

2. Crea `.env` a partir de `.env.example` y configura la clave secreta y los datos de PostgreSQL. En PowerShell:
   ```powershell
   Copy-Item .env.example .env
   ```
   Reemplaza los valores de ejemplo antes de iniciar el proyecto. No subas `.env` a Git.

3. **Aplicar migraciones**:
   ```bash
   python manage.py migrate
   ```

4. **Iniciar el servidor**:
   ```bash
   python manage.py runserver
   ```

5. Abrir **`http://127.0.0.1:8000`** en tu navegador.

---

## 📁 Estructura del Proyecto

- `run.bat` / `run.sh` - Scripts de inicio automático de 1 clic.
- `requirements.txt` - Lista de dependencias compatibles con cualquier sistema operativo.
- `.env.example` - Plantilla para variables de entorno opcionales.
- `manage.py` - Script de comandos principal de Django.
- `istte/` - Configuración principal del proyecto Django.
- `webapp/` - Aplicación principal y vistas.
- `templates/` - Plantillas HTML de la interfaz.
- `static/` - Archivos CSS, JS e imágenes del sitio.
- `media/` - Subidas de archivos multimedia.
