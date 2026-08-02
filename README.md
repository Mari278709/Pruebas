# Proyecto Django ISTTE

Este proyecto contiene la versión Django del portal institucional del Instituto Tecnológico Superior Tecnoecuatoriano.

Está preparado para ejecutarse **en cualquier computadora (Windows, macOS o Linux)** de forma automática y portátil.

---

## 🚀 Cómo Ejecutar en Cualquier PC

### Método Automático (Recomendado)

#### 🔹 En Windows:
Haz doble clic en `run.bat` o ejecuta en la consola:
```cmd
run.bat
```

#### 🔹 En Linux / macOS:
Abre la terminal y ejecuta:
```bash
chmod +x run.sh
./run.sh
```

*(El script crea automáticamente el entorno virtual `venv`, instala las dependencias de `requirements.txt`, aplica las migraciones y lanza el servidor).*

---

### Método Manual

1. **Crear y activar un entorno virtual**:
   - Windows: `python -m venv venv` y `venv\Scripts\activate`
   - Linux/Mac: `python3 -m venv venv` y `source venv/bin/activate`

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

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
