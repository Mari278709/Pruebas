from django.db import models
from django.shortcuts import get_object_or_404, render

PAGE_TEMPLATES = [
    'index',
    'autoridades',
    'organigrama',
    'planificacion_estrategica',
    'sedes_campus',
    'carreras',
    'validacion_experiencia',
    'detalle_carreras',
    'registro_carreras',
    'biblioteca',
    'portal_empleo',
    'asociacion_graduados',
    'soporte_tecnico',
    'unidad_titulacion',
    'cec_tecno',
    'bienestar',
    'vinculacion',
    'investigacion',
    'proceso_admision',
    'becas_incentivos',
    'inscripcion',
    'contacto',
]


def index(request):
    from .models import MediaItem, Noticia

    latest_media = MediaItem.objects.filter(published=True)[:3]
    latest_news = Noticia.objects.filter(published=True, status='publicado').order_by('-published_at')[:3]
    return render(request, 'index.html', {
        'latest_media': latest_media,
        'latest_news': latest_news,
    })


def autoridades(request):
    return render(request, 'autoridades.html')


def organigrama(request):
    return render(request, 'organigrama.html')


def planificacion_estrategica(request):
    return render(request, 'planificacion_estrategica.html')


def sedes_campus(request):
    return render(request, 'sedes_campus.html')


CARRERAS_DATA = {
    'desarrollo-software': {
        'title': 'Desarrollo de Software',
        'image': '/static/images/carreras/desarrollo-software.svg',
        'duration': '2 Años (4 Semestres)',
        'modality': 'Presencial y En Línea',
        'degree': 'Técnico Superior Tecnológico en Desarrollo de Software',
        'learn': [
            'Programación Web, Móvil y de Escritorio (Python, JS, Java)',
            'Modelamiento de Bases de Datos SQL y NoSQL (PostgreSQL, MongoDB)',
            'Metodologías de Ingeniería de Software (SCRUM y DevOps)',
            'Fundamentos de Ciberseguridad y Auditoría básica',
            'Despliegue de Aplicaciones en la Nube (AWS, GCP, Azure)'
        ],
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'profile': 'El profesional en Desarrollo de Software diseña, codifica y despliega soluciones web, móviles e híbridas utilizando los marcos de trabajo y estándares de desarrollo más demandados del sector tecnológico.',
        'malla': {
            'Primer Semestre': ['Algoritmos y Lógica de Programación', 'Introducción a las TIC', 'Matemática Discreta', 'Comunicación Oral y Escrita'],
            'Segundo Semestre': ['Programación Orientada a Objetos', 'Estructura de Datos', 'Bases de Datos Relacionales', 'Sistemas Operativos'],
            'Tercer Semestre': ['Desarrollo Web Frontend', 'Desarrollo Backend', 'Ingeniería de Software', 'Metodologías Ágiles de Desarrollo'],
            'Cuarto Semestre': ['Desarrollo de Aplicaciones Móviles', 'Computación en la Nube (Cloud)', 'Seguridad en Aplicaciones', 'Prácticas Preprofesionales'],
        },
        'campo': [
            'Desarrollador Full-Stack o Frontend/Backend',
            'Administrador y Modelador de Bases de Datos',
            'Especialista en QA (Quality Assurance) y Testing',
            'Arquitecto y Diseñador de Soluciones Cloud',
            'Consultor Tecnológico y Desarrollador Autónomo'
        ],
        'egreso': 'Al finalizar su formación, el egresado del ISTTE sabrá programar de manera limpia y estructurada, aplicar patrones de diseño, integrar APIs modernas, desplegar microservicios seguros y colaborar en entornos ágiles multidisciplinarios.'
    },
    'ciberseguridad': {
        'title': 'Ciberseguridad',
        'image': '/static/images/carreras/ciberseguridad.svg',
        'duration': '2.5 Años (5 Semestres)',
        'modality': 'Presencial',
        'degree': 'Tecnólogo Superior en Ciberseguridad',
        'learn': [
            'Seguridad de Redes e Infraestructuras Críticas',
            'Hacking Ético y Pruebas de Penetración (Pentesting)',
            'Análisis Forense Digital y Recuperación de Datos',
            'Gestión de Riesgos de Información y Gobernanza TI',
            'Seguridad en Infraestructura Cloud y Contenedores'
        ],
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'profile': 'El tecnólogo en Ciberseguridad diseña y ejecuta auditorías y planes de protección para resguardar la confidencialidad, integridad y disponibilidad de la información crítica de organizaciones y usuarios.',
        'malla': {
            'Primer Semestre': ['Redes y Telecomunicaciones I', 'Introducción a la Ciberseguridad', 'Criptografía Básica', 'Matemática Aplicada'],
            'Segundo Semestre': ['Redes y Telecomunicaciones II', 'Seguridad en Sistemas Operativos', 'Administración de Servidores', 'Legislación Informática y Delitos Informáticos'],
            'Tercer Semestre': ['Hacking Ético I', 'Seguridad en Redes Inalámbricas', 'Gestión de Incidentes y SOC', 'Auditoría y Control de Sistemas'],
            'Cuarto Semestre': ['Hacking Ético II (Avanzado)', 'Análisis Forense Digital', 'Seguridad Cloud y DevSecOps', 'Prácticas de Ciberdefensa'],
            'Quinto Semestre': ['Gobernanza de Ciberseguridad (ISO 27001)', 'Proyecto Integrador de Ciberseguridad', 'Ética Profesional y Cumplimiento', 'Ejercicios de Simulación de Ciberataque (Red/Blue Team)']
        },
        'campo': [
            'Analista de Seguridad en SOC (Security Operations Center)',
            'Especialista en Hacking Ético y Pentester de Infraestructuras',
            'Auditor de Seguridad de la Información corporativa',
            'Analista de Forense Digital y Perito Informático',
            'Administrador de Seguridad Perimetral y Firewalls'
        ],
        'egreso': 'El egresado será capaz de detectar brechas de seguridad, mitigar incidentes en tiempo real, auditar sistemas de información complejos, estructurar planes de recuperación de desastres y aplicar normativas de ciberseguridad vigentes.'
    },
    'administracion': {
        'title': 'Administración de Empresas',
        'image': '/static/images/carreras/administracion.svg',
        'duration': '2 Años (4 Semestres)',
        'modality': 'En Línea',
        'degree': 'Técnico Superior Tecnológico en Administración de Empresas',
        
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'profile': 'El profesional en Administración gestiona de forma integral y sostenible los recursos de organizaciones públicas o privadas, optimizando procesos y liderando estrategias de crecimiento en entornos digitales.',
        'malla': {
            'Primer Semestre': ['Administración General', 'Contabilidad Básica e Introducción Financiera', 'Matemática Financiera', 'Herramientas Ofimáticas Aplicadas'],
            'Segundo Semestre': ['Comportamiento Organizacional', 'Contabilidad de Costos', 'Microeconomía y Macroeconomía', 'Estadística Aplicada a Negocios'],
            'Tercer Semestre': ['Administración Financiera y Presupuestos', 'Marketing Digital y Estrategias Comerciales', 'Gestión de Talento Humano', 'Legislación Laboral, Mercantil y Tributaria'],
            'Cuarto Semestre': ['Planificación Estratégica y Formulación PEDI', 'Formulación y Evaluación de Proyectos', 'Auditoría Administrativa', 'Prácticas de Dirección e Inserción Laboral']
        },
        'campo': [
            'Administrador o Gerente de Pequeñas y Medianas Empresas (PYMEs)',
            'Coordinador de Operaciones y Logística Empresarial',
            'Analista Financiero y de Presupuestos corporativos',
            'Consultor de Estructuración de Procesos y Manuales de Gestión',
            'Emprendedor independiente de modelos de negocio modernos'
        ],
        'egreso': 'Al graduarse, el estudiante liderará equipos de trabajo, tomará decisiones estratégicas basadas en el análisis de datos financieros y de mercado, optimizará la cadena de valor e implementará planes estratégicos institucionales de forma proactiva.'
    },
    'escuela-conduccion': {
        'title': 'Escuela de Conducción Profesional',
        'image': '/static/images/carreras/escuela-conduccion.svg',
        'duration': '6 Meses (Licencias C, D y E)',
        'modality': 'Presencial y Semipresencial',
        'degree': 'Licencia de Conducir Profesional (Tipo C, D o E)',
        'learn': [
            'Leyes y Reglamentos de Tránsito y Transporte Terrestre',
            'Mecánica Básica y Mantenimiento de Flotas Vehiculares',
            'Educación Vial, Señalética e Infracciones de Tránsito',
            'Primeros Auxilios aplicados a siniestros viales',
            'Psicología y Atención al Cliente en Transporte de pasajeros/carga'
        ],
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'profile': 'Prepara conductores profesionales altamente capacitados, responsables y comprometidos con la seguridad vial y la excelencia en el servicio del transporte terrestre.',
        'malla': {
            'Fase Inicial (Mes 1 y 2)': ['Ley de Tránsito, Transporte Terrestre y Seguridad Vial', 'Reglamento de Tránsito e Infracciones', 'Educación Vial Obligatoria'],
            'Fase Técnica (Mes 3 y 4)': ['Mecánica Básica y Funcionamiento del Motor', 'Mantenimiento Preventivo del Vehículo', 'Primeros Auxilios y Manejo de Emergencias'],
            'Fase Práctica (Mes 5 y 6)': ['Psicología Aplicada a la Conducción', 'Prácticas de Conducción en Simuladores Homologados', 'Prácticas en Pista y Tráfico Real con Instructores Autorizados']
        },
        'campo': [
            'Conductor Profesional de Transporte de Pasajeros (Taxis, Buses)',
            'Conductor Profesional de Logística y Carga Pesada (Tráilers, Camiones)',
            'Supervisor de Logística y Flotas Vehiculares en empresas privadas',
            'Instructor de Conducción en Escuelas de Capacitación vial',
            'Asesor de Seguridad Vial y Prevención de Riesgos de Tránsito'
        ],
        'egreso': 'El egresado demuestra destrezas superiores de conducción técnica, opera vehículos pesados y especiales con alta seguridad, respeta la normativa nacional de tránsito y posee capacidad de reacción oportuna en situaciones de emergencia vial.'
    },
    'enfermeria': {
        'title': 'Enfermería',
        'image': '/static/images/carreras/enfermeria.svg',
        'duration': '2.5 Años (5 Semestres)',
        'modality': 'Presencial',
        'degree': 'Tecnólogo Superior en Enfermería',
        
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'profile': 'El profesional en Enfermería brinda cuidados integrales de salud a personas, familias y comunidades, aplicando conocimientos científicos, éticos y humanistas en los diferentes niveles de atención médica.',
        'malla': {
            'Primer Semestre': ['Anatomía y Fisiología Humana', 'Introducción a la Enfermería', 'Microbiología y Parasitología', 'Primeros Auxilios'],
            'Segundo Semestre': ['Enfermería Básica', 'Farmacología I', 'Epidemiología', 'Salud Pública'],
            'Tercer Semestre': ['Enfermería Médico-Quirúrgica I', 'Farmacología II', 'Nutrición y Dietética', 'Salud Mental'],
            'Cuarto Semestre': ['Enfermería Gineco-Obstétrica', 'Enfermería Pediátrica', 'Administración en Servicios de Enfermería', 'Prácticas Hospitalarias I'],
            'Quinto Semestre': ['Enfermería Comunitaria', 'Soporte Vital Avanzado', 'Ética y Deontología Profesional', 'Internado Rotativo de Enfermería']
        },
        'campo': [
            'Hospitales y Clínicas públicas y privadas',
            'Centros y Subcentros de Salud (Atención Primaria)',
            'Centros Geriátricos y de Cuidado Infantil',
            'Servicios de Salud Ocupacional en empresas',
            'Atención de enfermería domiciliaria e independiente'
        ],
        'egreso': 'El egresado de Enfermería del ISTTE estará capacitado para ejecutar procedures clínicos de enfermería con precisión, administrar tratamientos prescritos, colaborar en equipos de salud en emergencias y promover hábitos de vida saludables en la población.'
    }
}


def carreras(request):
    from .models import Carrera
    
    modalidad_filtro = request.GET.get('modalidad', None)
    
    # Obtener todas las carreras de la base de datos
    carreras_queryset = Carrera.objects.filter(published=True).order_by('title')
    
    # Filtrar por modalidad si es necesario
    if modalidad_filtro:
        modalidad = modalidad_filtro.lower()
        if modalidad == 'presencial':
            carreras_queryset = carreras_queryset.filter(modality__icontains='Presencial')
        elif modalidad == 'linea':
            carreras_queryset = carreras_queryset.filter(
                models.Q(modality__icontains='Línea') | models.Q(modality__icontains='Linea') | models.Q(modality__icontains='En Línea')
            )
    
    # Convertir queryset a lista de tuplas (slug, info_dict) para compatibilidad con template
    filtered_carreras = []
    for carrera in carreras_queryset:
        info = {
            'title': carrera.title,
            'image': carrera.image.url if carrera.image else '/static/images/carreras/default.svg',
            'duration': carrera.duration,
            'modality': carrera.modality,
            'degree': carrera.degree,
            'profile': carrera.profile or carrera.description,
            'description': carrera.description,
            'slug': carrera.slug,
        }

        # Si en CARRERAS_DATA hay información extendida para este slug, mezclarla
        try:
            slug_key = carrera.slug
            if slug_key in CARRERAS_DATA:
                external = CARRERAS_DATA[slug_key]
                # Añadir listas y campos ricos si no están en la DB
                for key in ('learn', 'campo', 'malla', 'egreso', 'video_url'):
                    if key in external and (key not in info or not info.get(key)):
                        info[key] = external.get(key)
        except Exception:
            # No fallar si hay problemas con slugs o datos externos
            pass

        filtered_carreras.append((carrera.slug, info))

    return render(request, 'carreras.html', {
        'carreras': filtered_carreras,
        'modalidad_filtro': modalidad_filtro
    })


def validacion_experiencia(request):
    return render(request, 'validacion_experiencia.html')


def detalle_carreras(request, career_slug):
    from django.shortcuts import redirect
    from django.urls import reverse
    from .models import Carrera
    
    career_slug = career_slug.lower()
    
    # Primero intentar buscar en la base de datos
    try:
        carrera = Carrera.objects.get(slug=career_slug, published=True)
        career_info = {
            'title': carrera.title,
            'image': carrera.image.url if carrera.image else '/static/images/carreras/default.svg',
            'profile_image': carrera.profile_image.url if carrera.profile_image else None,
            'duration': carrera.duration,
            'modality': carrera.modality,
            'degree': carrera.degree,
            'profile': carrera.profile or carrera.description,
            'description': carrera.description,
            'video_url': carrera.video_url,
            'slug': carrera.slug,
            'learn': carrera.learn or [],
            'campo': carrera.campo or [],
            'malla': carrera.malla or {},
            'egreso': carrera.egreso or carrera.profile or '',
        }
        return render(request, 'detalle_carreras.html', {
            'career_slug': career_slug,
            'career': career_info
        })
    except Carrera.DoesNotExist:
        # Si no existe en la BD, buscar en CARRERAS_DATA para compatibilidad
        if career_slug in CARRERAS_DATA:
            career_info = CARRERAS_DATA[career_slug]
            return render(request, 'detalle_carreras.html', {
                'career_slug': career_slug,
                'career': career_info
            })
        else:
            return redirect(reverse('carreras'))


def registro_carreras(request):
    return render(request, 'registro_carreras.html')


def biblioteca(request):
    return render(request, 'biblioteca.html')


def portal_empleo(request):
    return render(request, 'portal_empleo.html')


def asociacion_graduados(request):
    return render(request, 'asociacion_graduados.html')


def soporte_tecnico(request):
    return render(request, 'soporte_tecnico.html')


def unidad_titulacion(request):
    return render(request, 'unidad_titulacion.html')


def cec_tecno(request):
    return render(request, 'cec_tecno.html')


def bienestar(request):
    return render(request, 'bienestar.html')


def vinculacion(request):
    return render(request, 'vinculacion.html')


def investigacion(request):
    return render(request, 'investigacion.html')


def tecno_informativo(request):
    from .models import Noticia
    news_items = Noticia.objects.filter(published=True, status='publicado').order_by('-published_at')
    return render(request, 'tecno_informativo.html', {
        'news_items': news_items
    })


def noticia_detalle(request, slug):
    from .models import Noticia
    noticia = get_object_or_404(Noticia, slug=slug, published=True, status='publicado')
    return render(request, 'noticia_detalle.html', {
        'noticia': noticia
    })


def proceso_admision(request):
    return render(request, 'proceso_admision.html')


def becas_incentivos(request):
    return render(request, 'becas_incentivos.html')


def inscripcion(request):
    return render(request, 'inscripcion.html')


def contacto(request):
    return render(request, 'contacto.html')


def presentacion_institucional(request):
    return render(request, 'presentacion_institucional.html')


def aseguramiento_calidad(request):
    return render(request, 'aseguramiento_calidad.html')

def transparencia(request):
    return render(request, 'transparencia.html')


def aviso_legal(request):
    return render(request, 'aviso_legal.html')


def politica_privacidad(request):
    return render(request, 'politica_privacidad.html')


def multimedia(request):
    from .models import MediaItem, Noticia

    media_items = MediaItem.objects.filter(published=True)
    news_items = Noticia.objects.filter(published=True, status='publicado').order_by('-published_at')
    return render(request, 'multimedia.html', {
        'media_items': media_items,
        'news_items': news_items,
    })


def upload_media(request):
    from .forms import MediaItemForm

    success = False
    if request.method == 'POST':
        form = MediaItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            form = MediaItemForm()
    else:
        form = MediaItemForm()

    return render(request, 'upload_media.html', {
        'form': form,
        'success': success,
    })
