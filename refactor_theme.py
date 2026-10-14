import os
import glob

# Directorio de templates
TEMPLATES_DIR = r"d:\Git GitHub\Busy\Pruebas\templates"

# Archivos a excluir
EXCLUDE_FILES = ["base.html", "index.html"]

# Reglas de reemplazo masivo
REPLACEMENTS = {
    # Eliminar bg-white y bordes claros por tarjetas de cristal
    'bg-white': 'glass-card',
    'border border-light-subtle': 'border-0',
    'border-light-subtle': 'border-0',
    'shadow-sm': '', # glass-card ya tiene sombra
    
    # Textos azules/oscuros a blancos
    'text-primary': 'text-white',
    'text-dark': 'text-white',
    
    # Textos secundarios y succes a neon/blancos
    'text-success': 'text-neon',
    
    # Badges
    'bg-success': 'badge-neon',
    'bg-primary': 'badge-neon',
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for old, new in REPLACEMENTS.items():
        content = content.replace(old, new)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    html_files = glob.glob(os.path.join(TEMPLATES_DIR, "**", "*.html"), recursive=True)
    modified_count = 0
    
    for filepath in html_files:
        basename = os.path.basename(filepath)
        if basename in EXCLUDE_FILES:
            continue
            
        if process_file(filepath):
            modified_count += 1
            print(f"Modificado: {basename}")
            
    print(f"Se modificaron {modified_count} archivos en total.")

if __name__ == "__main__":
    main()
