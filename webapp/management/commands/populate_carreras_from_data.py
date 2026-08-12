from django.core.management.base import BaseCommand
from webapp.views import CARRERAS_DATA
from webapp.models import Carrera

class Command(BaseCommand):
    help = 'Rellena campos learn/campo/malla/egreso en Carrera usando CARRERAS_DATA cuando el slug coincide'

    def handle(self, *args, **options):
        updated = 0
        for slug, info in CARRERAS_DATA.items():
            c = None
            # intentar por slug primero
            try:
                c = Carrera.objects.get(slug=slug)
            except Carrera.DoesNotExist:
                # intentar por título (coincidencia aproximada)
                title = info.get('title', '')
                if title:
                    qs = Carrera.objects.filter(title__icontains=title)
                    if qs.exists():
                        c = qs.first()

            if c:
                c.learn = info.get('learn', [])
                c.campo = info.get('campo', [])
                c.malla = info.get('malla', {})
                c.egreso = info.get('egreso', '')
                c.save()
                updated += 1
                self.stdout.write(self.style.SUCCESS(f'Updated: {c.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Not found in DB: {slug} / {info.get("title")}'))
        self.stdout.write(self.style.SUCCESS(f'Done. Updated {updated} entries.'))
