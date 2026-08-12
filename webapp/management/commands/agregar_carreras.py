from django.core.management.base import BaseCommand
from webapp.models import Carrera


class Command(BaseCommand):
    help = 'Agrega todas las carreras del instituto a la base de datos'

    def handle(self, *args, **options):
        carreras_data = [
            # CARRERAS ADMINISTRATIVAS
            {
                'title': 'Administración de Empresas',
                'duration': '2 Años (4 Semestres)',
                'modality': 'En Línea',
                'degree': 'Técnico Superior Tecnológico en Administración de Empresas',
                'description': 'Gestión integral y sostenible de recursos organizacionales en entornos digitales.',
                'profile': 'El profesional en Administración gestiona de forma integral y sostenible los recursos de organizaciones públicas o privadas, optimizando procesos y liderando estrategias de crecimiento en entornos digitales.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Contabilidad',
                'duration': '2 Años (4 Semestres)',
                'modality': 'En Línea',
                'degree': 'Técnico Superior Tecnológico en Contabilidad',
                'description': 'Registro, análisis e interpretación de la información financiera de las organizaciones.',
                'profile': 'El profesional en Contabilidad registra, analiza e interpreta la información financiera de las organizaciones, asegurando transparencia, cumplimiento normativo y apoyo a la toma de decisiones estratégicas.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Planificación y Gestión',
                'duration': '2 Años (4 Semestres)',
                'modality': 'Presencial y En Línea',
                'degree': 'Técnico Superior Tecnológico en Planificación y Gestión',
                'description': 'Desarrollo de planes estratégicos y gestión de proyectos en organizaciones.',
                'profile': 'El profesional en Planificación y Gestión diseña e implementa planes estratégicos institucionales, gestiona proyectos complejos y coordina equipos multidisciplinarios para el logro de objetivos organizacionales.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Auditoría',
                'duration': '2 Años (4 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico Superior Tecnológico en Auditoría',
                'description': 'Evaluación y control de procesos contables, financieros y operacionales.',
                'profile': 'El profesional en Auditoría evalúa y controla procesos contables, financieros y operacionales de las organizaciones, asegurando cumplimiento normativo, eficiencia y transparencia en la gestión de recursos.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Seguridad e Higiene del Trabajo',
                'duration': '2 Años (4 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico Superior Tecnológico en Seguridad e Higiene del Trabajo',
                'description': 'Prevención de riesgos laborales y promoción de ambientes de trabajo seguros y saludables.',
                'profile': 'El profesional en Seguridad e Higiene del Trabajo identifica peligros, evalúa riesgos laborales e implementa medidas preventivas y correctivas para garantizar ambientes seguros, saludables y productivos.',
                'published': True,
                'featured': False,
            },
            # CARRERAS DE SALUD
            {
                'title': 'Técnico en Enfermería',
                'duration': '2.5 Años (5 Semestres)',
                'modality': 'Presencial',
                'degree': 'Tecnólogo Superior en Enfermería',
                'description': 'Cuidados integrales de salud a personas, familias y comunidades.',
                'profile': 'El profesional en Enfermería brinda cuidados integrales de salud a personas, familias y comunidades, aplicando conocimientos científicos, éticos y humanistas en los diferentes niveles de atención médica.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Rehabilitación Física',
                'duration': '2.5 Años (5 Semestres)',
                'modality': 'Presencial',
                'degree': 'Tecnólogo Superior en Rehabilitación Física',
                'description': 'Recuperación funcional y máxima autonomía en personas con discapacidad física.',
                'profile': 'El profesional en Rehabilitación Física restaura la función, minimiza la discapacidad y optimiza la calidad de vida de personas con condiciones músculo-esqueléticas, neurológicas y cardiopulmonares.',
                'published': True,
                'featured': False,
            },
            # BIENESTAR Y SERVICIOS
            {
                'title': 'Entrenamiento Deportivo',
                'duration': '2 Años (4 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico Superior Tecnológico en Entrenamiento Deportivo',
                'description': 'Planificación y ejecución de programas de entrenamiento deportivo de alto rendimiento.',
                'profile': 'El profesional en Entrenamiento Deportivo diseña, planifica y ejecuta programas científicos de entrenamiento para potenciar el rendimiento físico y técnico de atletas individuales y equipos competitivos.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Desarrollo Infantil Integral',
                'duration': '2 Años (4 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico Superior Tecnológico en Desarrollo Infantil Integral',
                'description': 'Atención educativa, nutritiva y emocional de niños en primera infancia.',
                'profile': 'El profesional en Desarrollo Infantil Integral promueve el crecimiento y aprendizaje holístico de niños desde 0 a 5 años, favoreciendo su desarrollo cognitivo, social, emocional y motriz en contextos educativos y comunitarios.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Producción de Pastelería e Imagen',
                'duration': '1.5 Años (3 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico en Producción de Pastelería e Imagen',
                'description': 'Elaboración artística de productos de pastelería y repostería gourmet.',
                'profile': 'El profesional en Producción de Pastelería e Imagen elabora y decora productos de pastelería fina, tartas artísticas y repostería gourmet con técnicas avanzadas, aplicando principios de higiene y presentación estética profesional.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Gastronomía',
                'duration': '2 Años (4 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico Superior Tecnológico en Gastronomía',
                'description': 'Preparación profesional de alimentos y gestión de servicios culinarios.',
                'profile': 'El profesional en Gastronomía prepara y presenta alimentos con técnicas culinarias contemporáneas, gestiona servicios de alimentación en establecimientos y emprende negocios gastronómicos de excelencia.',
                'published': True,
                'featured': False,
            },
            # CIENCIAS AGROPECUARIAS
            {
                'title': 'Nutrición Animal',
                'duration': '2 Años (4 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico Superior Tecnológico en Nutrición Animal',
                'description': 'Manejo nutricional de especies ganaderas para optimizar producción.',
                'profile': 'El profesional en Nutrición Animal formula dietas equilibradas, maneja sistemas de alimentación animal y optimiza la producción ganadera aplicando principios de nutrición, salud y sostenibilidad ambiental.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Acuicultura',
                'duration': '2 Años (4 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico Superior Tecnológico en Acuicultura',
                'description': 'Cultivo y reproducción controlada de especies acuáticas.',
                'profile': 'El profesional en Acuicultura cultiva y reproduce de forma controlada especies acuáticas, manejando sistemas de calidad de agua, sanidad animal y reproducción para optimizar la producción sostenible.',
                'published': True,
                'featured': False,
            },
            # CARRERAS AUTOMOTRICES
            {
                'title': 'Mecánica Automotriz',
                'duration': '1.5 Años (3 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico en Mecánica Automotriz',
                'description': 'Reparación, mantenimiento y diagnóstico de sistemas vehiculares.',
                'profile': 'El profesional en Mecánica Automotriz diagnostica, repara y mantiene sistemas mecánicos, eléctricos y electrónicos de vehículos, aplicando tecnología automotriz moderna y normas de seguridad industrial.',
                'published': True,
                'featured': False,
            },
            {
                'title': 'Electromecánica Automotriz',
                'duration': '2 Años (4 Semestres)',
                'modality': 'Presencial',
                'degree': 'Técnico Superior Tecnológico en Electromecánica Automotriz',
                'description': 'Integración de sistemas mecánicos y electrónicos en vehículos modernos.',
                'profile': 'El profesional en Electromecánica Automotriz diagnostica y repara sistemas integrados mecánicos, eléctricos y electrónicos de vehículos de última generación, realizando mantenimiento preventivo y correctivo.',
                'published': True,
                'featured': False,
            },
        ]

        created_count = 0
        skipped_count = 0

        for carrera_data in carreras_data:
            carrera, created = Carrera.objects.get_or_create(
                title=carrera_data['title'],
                defaults=carrera_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Creada: {carrera.title}')
                )
            else:
                skipped_count += 1
                self.stdout.write(
                    self.style.WARNING(f'⊘ Ya existe: {carrera.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Proceso completado: {created_count} carreras creadas, {skipped_count} carreras ya existentes'
            )
        )
