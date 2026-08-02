import os

files = {
    r"d:\Git GitHub\Busy\Pruebas\templates\detalle_carreras.html": [
        ('Ej: Jesus Pacheco', 'Ej: Mariuxi Minda'),
        ('jesus@ejemplo.com', 'mariuxi@ejemplo.com'),
        ('btn btn-success btn-lg w-100', 'btn-neon-solid btn-lg w-100'),
        ('btn btn-success w-100 py-2 mt-2 fw-bold text-white text-uppercase" style="background-color: var(--istte-green-accent);"', 'btn-neon-solid w-100 py-2 mt-2 fw-bold text-uppercase"'),
    ],
    r"d:\Git GitHub\Busy\Pruebas\templates\inscripcion.html": [
        ('Ej: Jesus Pacheco', 'Ej: Mariuxi Minda'),
    ],
    r"d:\Git GitHub\Busy\Pruebas\templates\contacto.html": [
        ('Ej: Jesus Pacheco', 'Ej: Mariuxi Minda'),
    ],
    r"d:\Git GitHub\Busy\Pruebas\templates\planificacion_estrategica.html": [
        ('btn btn-lg btn-success text-white py-3 px-4 fw-bold shadow', 'btn-neon-solid btn-lg py-3 px-4 fw-bold shadow'),
    ],
    r"d:\Git GitHub\Busy\Pruebas\templates\carreras.html": [
        ('btn btn-sm btn-success flex-grow-1 text-white fw-bold" style="background-color: var(--istte-green-accent);"', 'btn-neon-solid btn-sm flex-grow-1 fw-bold"'),
    ]
}

for filepath, replacements in files.items():
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        for old, new in replacements:
            content = content.replace(old, new)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Modificado: {os.path.basename(filepath)}")
    else:
        print(f"Archivo no encontrado: {filepath}")
