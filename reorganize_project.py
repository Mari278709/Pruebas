from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
legacy = root / 'legacy_site'
legacy.mkdir(exist_ok=True)

# Move legacy static HTML files to legacy_site
for html_file in root.glob('*.html'):
    if html_file.name == 'base.html':
        continue
    if html_file.name == 'manage.py':
        continue
    shutil.move(str(html_file), str(legacy / html_file.name))

# Move the local renderer to legacy
renderer = root / 'render_local.py'
if renderer.exists():
    shutil.move(str(renderer), str(legacy / 'render_local.py'))

# Remove empty generated template directories
webapp_templates = root / 'webapp' / 'templates'
if webapp_templates.exists() and webapp_templates.is_dir():
    for child in webapp_templates.iterdir():
        if child.is_dir() and not any(child.iterdir()):
            child.rmdir()
    if not any(webapp_templates.iterdir()):
        webapp_templates.rmdir()

print('Reorganización completada')
