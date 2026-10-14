#!/bin/bash
echo "===================================================="
echo "Iniciando Proyecto Django ISTTE en Linux/macOS..."
echo "===================================================="

# 1. Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
fi

# 2. Activar entorno virtual
source venv/bin/activate

# 3. Instalar/Actualizar dependencias
echo "Instalando dependencias desde requirements.txt..."
pip install -r requirements.txt

# 4. Aplicar migraciones
echo "Aplicando migraciones de base de datos..."
python manage.py migrate

# 5. Iniciar servidor
echo "===================================================="
echo "Servidor iniciado en http://127.0.0.1:8000/"
echo "Presiona Ctrl+C para detener el servidor."
echo "===================================================="
python manage.py runserver 127.0.0.1:8000
