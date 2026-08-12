from django.core.management.base import BaseCommand
from webapp.models import Carrera

class Command(BaseCommand):
    help = 'Lista slugs y títulos de las carreras'

    def handle(self, *args, **options):
        for c in Carrera.objects.order_by('title'):
            self.stdout.write(f"{c.slug} - {c.title}")
        self.stdout.write(self.style.SUCCESS(f'Total: {Carrera.objects.count()}'))
