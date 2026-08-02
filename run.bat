@echo off
echo ====================================================
echo Iniciando Proyecto Django ISTTE en Windows...
echo ====================================================

REM 1. Crear entorno virtual si no existe
if not exist "venv" (
    echo Creando entorno virtual...
    python -m venv venv
)

REM 2. Activar entorno virtual
call venv\Scripts\activate

REM 3. Instalar/Actualizar dependencias
echo Instalando dependencias desde requirements.txt...
pip install -r requirements.txt

REM 4. Aplicar migraciones
echo Aplicando migraciones de base de datos...
python manage.py migrate

REM 5. Iniciar servidor
echo ====================================================
echo Servidor iniciado en http://127.0.0.1:8000/
echo Presiona Ctrl+C para detener el servidor.
echo ====================================================
python manage.py runserver 127.0.0.1:8000
