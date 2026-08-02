from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Inscripcion

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
    from .models import MediaItem

    latest_media = MediaItem.objects.filter(published=True)[:3]
    return render(request, 'index.html', {
        'latest_media': latest_media,
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
        'learn': [
            'Planificación Estratégica y PEDI corporativo',
            'Gestión Financiera, Presupuestos y Contabilidad de Costos',
            'Marketing Digital, Ventas y Publicidad en Redes',
            'Dirección de Talento Humano y Clima Organizacional',
            'Emprendimiento, Modelos de Negocio e Innovación'
        ],
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
    }
}


def carreras(request):
    modalidad_filtro = request.GET.get('modalidad', None)
    filtered_carreras = []
    
    for slug, info in CARRERAS_DATA.items():
        if modalidad_filtro:
            m = modality_slug = modalidad_filtro.lower()
            if m == 'presencial' and 'presencial' in info['modality'].lower():
                filtered_carreras.append((slug, info))
            elif m == 'linea' and ('línea' in info['modality'].lower() or 'linea' in info['modality'].lower()):
                filtered_carreras.append((slug, info))
        else:
            filtered_carreras.append((slug, info))
            
    return render(request, 'carreras.html', {
        'carreras': filtered_carreras,
        'modalidad_filtro': modalidad_filtro
    })


def validacion_experiencia(request):
    return render(request, 'validacion_experiencia.html')

from django.http import JsonResponse

def api_carreras(request):
    """
    Endpoint para que el frontend de React consuma la data de las carreras.
    """
    return JsonResponse({'carreras': CARRERAS_DATA})

def api_media(request):
    from .models import MediaItem
    media = MediaItem.objects.filter(published=True).order_by('-created_at')[:3]
    media_list = []
    for item in media:
        media_list.append({
            'title': item.title,
            'description': item.description,
            'image_url': item.image.url if item.image else None,
            'video_url': item.video.url if item.video else None,
            'created_at': item.created_at.isoformat()
        })
    return JsonResponse({'media': media_list})



def detalle_carreras(request, career_slug):
    from django.shortcuts import redirect
    from django.urls import reverse
    
    career_slug = career_slug.lower()
    if career_slug not in CARRERAS_DATA:
        return redirect(reverse('carreras'))
        
    career_info = CARRERAS_DATA[career_slug]
    return render(request, 'detalle_carreras.html', {
        'career_slug': career_slug,
        'career': career_info
    })


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
    from .models import MediaItem
    latest_media = MediaItem.objects.filter(published=True)
    return render(request, 'tecno_informativo.html', {
        'news_items': latest_media
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


def gaceta_institucional(request):
    return render(request, 'gaceta_institucional.html')


def transparencia(request):
    return render(request, 'transparencia.html')


def aviso_legal(request):
    return render(request, 'aviso_legal.html')


def politica_privacidad(request):
    return render(request, 'politica_privacidad.html')


def multimedia(request):
    from .models import MediaItem

    media_items = MediaItem.objects.filter(published=True)
    return render(request, 'multimedia.html', {
        'media_items': media_items,
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


@csrf_exempt
def api_inscripcion(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            inscripcion = Inscripcion.objects.create(
                nombres=data.get('nombres', ''),
                apellidos=data.get('apellidos', ''),
                cedula=data.get('cedula', ''),
                telefono=data.get('telefono', ''),
                correo=data.get('correo', ''),
                carrera=data.get('carrera', ''),
                modalidad=data.get('modalidad', '')
            )
            return JsonResponse({'status': 'success', 'message': 'Inscripción recibida con éxito.', 'id': inscripcion.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)
