from django.shortcuts import render
from .models import MediaItem
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

CYBERSECURITY_IMAGE = '/static/images/carreras/CIBERSEGURIDAD.jpg'

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
            'Despliegue de Aplicaciones en la Nube (AWS, GCP, Azure)',
        ],
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'profile': (
            'El profesional en Desarrollo de Software diseña, codifica y'
            ' despliega soluciones web, móviles e híbridas utilizando los marcos'
            ' de trabajo y estándares de desarrollo más demandados del sector'
            ' tecnológico.'
        ),
        'malla': {
            'Primer Semestre': [
                'Algoritmos y Lógica de Programación',
                'Introducción a las TIC',
                'Matemática Discreta',
                'Comunicación Oral y Escrita',
            ],
            'Segundo Semestre': [
                'Programación Orientada a Objetos',
                'Estructura de Datos',
                'Bases de Datos Relacionales',
                'Sistemas Operativos',
            ],
            'Tercer Semestre': [
                'Desarrollo Web Frontend',
                'Desarrollo Backend',
                'Ingeniería de Software',
                'Metodologías Ágiles de Desarrollo',
            ],
            'Cuarto Semestre': [
                'Desarrollo de Aplicaciones Móviles',
                'Computación en la Nube (Cloud)',
                'Seguridad en Aplicaciones',
                'Prácticas Preprofesionales',
            ],
        },
        'campo': [
            'Desarrollador Full-Stack o Frontend/Backend',
            'Administrador y Modelador de Bases de Datos',
            'Especialista en QA (Quality Assurance) y Testing',
            'Arquitecto y Diseñador de Soluciones Cloud',
            'Consultor Tecnológico y Desarrollador Autónomo',
        ],
        'egreso': (
            'Al finalizar su formación, el egresado del ISTTE sabrá programar'
            ' de manera limpia y estructurada, aplicar patrones de diseño,'
            ' integrar APIs modernas, desplegar microservicios seguros y'
            ' colaborar en entornos ágiles multidisciplinarios.'
        ),
    },
    'ciberseguridad': {
        'title': 'Ciberseguridad',
        'image': CYBERSECURITY_IMAGE,
        'duration': '2.5 Años (5 Semestres)',
        'modality': 'Presencial',
        'degree': 'Tecnólogo Superior en Ciberseguridad',
        'learn': [
            'Seguridad de Redes e Infraestructuras Críticas',
            'Hacking Ético y Pruebas de Penetración (Pentesting)',
            'Análisis Forense Digital y Recuperación de Datos',
            'Gestión de Riesgos de Información y Gobernanza TI',
            'Seguridad en Infraestructura Cloud y Contenedores',
        ],
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'profile': (
            'El tecnólogo en Ciberseguridad diseña y ejecuta auditorías y'
            ' planes de protección para resguardar la confidencialidad,'
            ' integridad y disponibilidad de la información crítica de'
            ' organizaciones y usuarios.'
        ),
        'malla': {
            'Primer Semestre': [
                'Redes y Telecomunicaciones I',
                'Introducción a la Ciberseguridad',
                'Criptografía Básica',
                'Matemática Aplicada',
            ],
            'Segundo Semestre': [
                'Redes y Telecomunicaciones II',
                'Seguridad en Sistemas Operativos',
                'Administración de Servidores',
                'Legislación Informática y Delitos Informáticos',
            ],
            'Tercer Semestre': [
                'Hacking Ético I',
                'Seguridad en Redes Inalámbricas',
                'Gestión de Incidentes y SOC',
                'Auditoría y Control de Sistemas',
            ],
            'Cuarto Semestre': [
                'Hacking Ético II (Avanzado)',
                'Análisis Forense Digital',
                'Seguridad Cloud y DevSecOps',
                'Prácticas de Ciberdefensa',
            ],
            'Quinto Semestre': [
                'Gobernanza de Ciberseguridad (ISO 27001)',
                'Proyecto Integrador de Ciberseguridad',
                'Ética Profesional y Cumplimiento',
                (
                    'Ejercicios de Simulación de Ciberataque (Red/Blue'
                    ' Team)'
                ),
            ],
        },
        'campo': [
            'Analista de Seguridad en SOC (Security Operations Center)',
            'Especialista en Hacking Ético y Pentester de Infraestructuras',
            'Auditor de Seguridad de la Información corporativa',
            'Analista de Forense Digital y Perito Informático',
            'Administrador de Seguridad Perimetral y Firewalls',
        ],
        'egreso': (
            'El egresado será capaz de detectar brechas de seguridad, mitigar'
            ' incidentes en tiempo real, auditar sistemas de información'
            ' complejos, estructurar planes de recuperación de desastres y'
            ' aplicar normativas de ciberseguridad vigentes.'
        ),
    },
    'administracion': {
        'title': 'Administración de Empresas',
        'image': '/static/images/carreras/administracion.svg',
        'duration': '2 Años (4 Semestres)',
        'modality': 'En Línea',
        'degree': (
            'Técnico Superior Tecnológico en Administración de Empresas'
        ),
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'profile': (
            'El profesional en Administración gestiona de forma integral y'
            ' sostenible los recursos de organizaciones públicas o privadas,'
            ' optimizando procesos y liderando estrategias de crecimiento en'
            ' entornos digitales.'
        ),
        'malla': {
            'Primer Semestre': [
                'Administración General',
                'Contabilidad Básica e Introducción Financiera',
                'Matemática Financiera',
                'Herramientas Ofimáticas Aplicadas',
            ],
            'Segundo Semestre': [
                'Comportamiento Organizacional',
                'Contabilidad de Costos',
                'Microeconomía y Macroeconomía',
                'Estadística Aplicada a Negocios',
            ],
            'Tercer Semestre': [
                'Administración Financiera y Presupuestos',
                'Marketing Digital y Estrategias Comerciales',
                'Gestión de Talento Humano',
                'Legislación Laboral, Mercantil y Tributaria',
            ],
            'Cuarto Semestre': [
                'Planificación Estratégica y Formulación PEDI',
                'Formulación y Evaluación de Proyectos',
                'Auditoría Administrativa',
                'Prácticas de Dirección e Inserción Laboral',
            ],
        },
        'campo': [
            (
                'Administrador o Gerente de Pequeñas y Medianas Empresas'
                ' (PYMEs)'
            ),
            'Coordinador de Operaciones y Logística Empresarial',
            'Analista Financiero y de Presupuestos corporativos',
            (
                'Consultor de Estructuración de Procesos y Manuales de'
                ' Gestión'
            ),
            'Emprendedor independiente de modelos de negocio modernos',
        ],
        'egreso': (
            'Al graduarse, el estudiante liderará equipos de trabajo, tomará'
            ' decisiones estratégicas basadas en el análisis de datos'
            ' financieros y de mercado, optimizará la cadena de valor e'
            ' implementará planes estratégicos institucionales de forma'
            ' proactiva.'
        ),
    },
   'escuela-conduccion': {
        'title': 'Escuela de Conducción Profesional',
        'image': '/static/images/carreras/escuela-conduccion.svg',
        'duration': 'Capacitación Continua y Licencias Profesionales',
        'modality': 'Presencial y Semipresencial',
        'degree': 'Licencias de Conducir Profesionales (Tipo C y C1) y Certificaciones Técnicas',
        'profile': (
            'La Escuela de Conducción Profesional ofrece cursos de capacitación '
            'para acceder a licencias de manejo profesional en las categorías C y C1. También está '
            'acreditada para dictar cursos de recuperación de puntos y emitir certificados de exámenes '
            'psicosensométricos.'
        ),
        'descripcion_general': (
            'La escuela ofrece cursos de capacitación para acceder a licencias de manejo profesional '
            'en las categorías C y C1. También está acreditada para dictar cursos de recuperación de '
            'puntos y emitir certificados de exámenes psicosensométricos.'
        ),
        'licencias': {
            'licencia_c': {
                'titulo': 'Licencia tipo C',
                'descripcion': (
                    'Permite conducir taxis convencionales, ejecutivos, camionetas livianas o mixtas '
                    'de hasta 3500 kg y hasta 8 pasajeros, vehículos de transporte de pasajeros de no '
                    'más de 25 asientos, y vehículos del tipo «B».'
                ),
                'costo': '$938.43',
                'duracion': '6 meses',
                'formas_pago': [
                    'Contado',
                    'Tarjeta de crédito hasta 6 meses sin intereses',
                    'Convenio de pago',
                ],
                'documentos': [
                    'Título de bachiller o acta de grado notariado, o pase de año de Cuarto Curso',
                    'Dos copias a color de la cédula de identidad y papeleta de votación',
                    'Dos copias a color del certificado de tipo sanguíneo (Cruz Roja)',
                    'Dos fotos a color tamaño carnet (3 cm x 3.5 cm)',
                    'Certificado de antecedentes personales (Récord Policial)',
                    'Planilla de luz (original o copia)',
                ],
                'horarios_teoricos': {
                    'lunes_viernes': {
                        'matutino': '8:00 a 11:00',
                        'nocturno': '18:30 a 21:30',
                    },
                    'fines_semana': 'Sábado y domingo de 7:30 a 15:45 (Intensivo)',
                },
                'horarios_practicos': {
                    'lunes_viernes': '2 horas diarias',
                    'fines_semana': '5 horas diarias (sábados y domingos)',
                },
            },
            'licencia_c1': {
                'titulo': 'Licencia tipo C1',
                'descripcion': (
                    'Permite la conducción de vehículos del Estado, de emergencia (ambulancias) '
                    'y de seguridad (Policía, Fuerzas Armadas y Metropolitanos).'
                ),
                'costo': '$938.43',
                'duracion': '6 meses',
                'formas_pago': [
                    'Contado',
                    'Tarjeta de crédito hasta 6 meses sin intereses',
                    'Convenio de pago',
                ],
                'documentos': [
                    'Mismos requisitos exigidos para la Licencia Tipo C',
                    'Licencia tipo B con al menos 2 años de antigüedad',
                ],
                'horarios_teoricos': {
                    'lunes_viernes': {
                        'matutino': '8:00 a 11:00',
                        'nocturno': '18:30 a 21:30',
                    },
                    'fines_semana': 'Sábado y domingo de 7:30 a 15:45 (Intensivo)',
                },
                'horarios_practicos': {
                    'lunes_viernes': '2 horas diarias',
                    'fines_semana': '5 horas diarias (sábados y domingos)',
                },
            },
            'convalidacion_c1': {
                'titulo': 'Convalidación Licencia C1 (en 2 meses)',
                'requisitos': [
                    'Licencia tipo C con al menos 2 años de antigüedad',
                ],
                'costo': '$391.00',
                'duracion': '2 meses',
                'formas_pago': [
                    'Contado',
                    'Tarjeta de crédito',
                    'Convenio de pago directo',
                ],
                'documentos': [
                    'Título de bachiller o acta de grado notariado, o pase de año de Cuarto Curso',
                    'Dos copias a color de la cédula de identidad y papeleta de votación',
                    'Dos copias a color del certificado de tipo sanguíneo (Cruz Roja)',
                    'Dos fotos a color tamaño carnet (3 cm x 3.5 cm)',
                    'Certificado de antecedentes personales (Récord Policial)',
                    'Planilla de luz (original o copia)',
                    'Certificado de conductor emitido por la ANT',
                    'En caso de tener menos de 5 años con la licencia, presentar récord académico, malla curricular o contenido de materias (solicitado en la escuela de origen, en originales)',
                    'Copia de la licencia tipo C (2 copias a color)',
                ],
                'horarios_teoricos': {
                    'lunes_viernes': {
                        'matutino': '8:00 a 11:00',
                        'nocturno': '18:30 a 21:30',
                    },
                    'fines_semana': 'Sábado y domingo de 7:30 a 15:45 (Intensivo)',
                },
                'horarios_practicos': {
                    'lunes_viernes': '2 horas diarias',
                    'fines_semana': '5 horas diarias (sábados y domingos)',
                },
            },
        },
        'examenes_adicionales': {
            'Examen Psicosensométrico': '$20.00',
            'Examen Médico': '$25.00',
        },
        'learn': [
            'Leyes, Ley Orgánica de Transporte Terrestre, Tránsito y Seguridad Vial',
            'Mecánica Básica, Diésel y Mantenimiento Preventivo de Flotas',
            'Educación, Señalética y Seguridad Vial',
            'Primeros Auxilios y Gestión de Emergencias en Carretera',
            'Psicología Aplicada, Ética y Atención al Cliente en Transporte de Pasajeros y Carga',
            'Técnicas de Conducción Defensiva y Operación de Vehículos Pesados',
        ],
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'malla': {
            'Módulo Teórico - Normativo': [
                'Ley Orgánica de Transporte Terrestre, Tránsito y Seguridad Vial',
                'Reglamento General Aplicable e Infracciones',
                'Educación Vial y Señalética Urbana y de Carretera',
                'Ética Profesional y Relaciones Humanas',
            ],
            'Módulo Técnico y Mecánico': [
                'Mecánica Básica y Funcionamiento de Motores a Gasolina/Diésel',
                'Mantenimiento Preventivo y Correctivo de Unidades',
                'Primeros Auxilios y Soporte Básico de Emergencias Viales',
                'Geografía Urbana y Rutas Nacionales',
            ],
            'Módulo Práctico de Manejo': [
                'Psicología Aplicada a la Conducción y Manejo del Estrés',
                'Prácticas de Manejo en Simuladores Homologados',
                'Prácticas en Pista de Maniobras y Tránsito Real',
                'Técnicas de Manejo Defensivo y Económico',
            ],
        },
        'campo': [
            'Conductor Profesional de Transporte Comercial (Taxis, Camionetas)',
            'Conductor Profesional de Transporte Urbano, Interprovincial y Escolar (Buses)',
            'Operador de Transporte de Carga Pesada y Combinados (Tráilers, Volquetas)',
            'Supervisor de Logística, Rutas y Flotas Vehiculares Corporativas',
            'Asesor y Promotor de Programas de Seguridad Vial y Prevención de Riesgos',
        ],
        'egreso': (
            'El participante graduado domina las destrezas de conducción técnica y defensiva, '
            'conoce exhaustivamente la legislación vial ecuatoriana, opera unidades de transporte '
            'con responsabilidad y cuenta con la capacidad técnica para actuar ante fallas mecánicas '
            'o eventualidades en carretera.'
        ),
    },
    'enfermeria': {
        'title': 'Enfermería',
        'image': '/static/images/carreras/enfermeria.svg',
        'duration': '2.5 Años (5 Semestres)',
        'modality': 'Presencial',
        'degree': 'Tecnólogo Superior en Enfermería',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'profile': (
            'El profesional en Enfermería brinda cuidados integrales de salud'
            ' a personas, familias y comunidades, aplicando conocimientos'
            ' científicos, éticos y humanistas en los diferentes niveles de'
            ' atención médica.'
        ),
        'malla': {
            'Primer Semestre': [
                'Anatomía y Fisiología Humana',
                'Introducción a la Enfermería',
                'Microbiología y Parasitología',
                'Primeros Auxilios',
            ],
            'Segundo Semestre': [
                'Enfermería Básica',
                'Farmacología I',
                'Epidemiología',
                'Salud Pública',
            ],
            'Tercer Semestre': [
                'Enfermería Médico-Quirúrgica I',
                'Farmacología II',
                'Nutrición y Dietética',
                'Salud Mental',
            ],
            'Cuarto Semestre': [
                'Enfermería Gineco-Obstétrica',
                'Enfermería Pediátrica',
                'Administración en Servicios de Enfermería',
                'Prácticas Hospitalarias I',
            ],
            'Quinto Semestre': [
                'Enfermería Comunitaria',
                'Soporte Vital Avanzado',
                'Ética y Deontología Profesional',
                'Internado Rotativo de Enfermería',
            ],
        },
        'campo': [
            'Hospitales y Clínicas públicas y privadas',
            'Centros y Subcentros de Salud (Atención Primaria)',
            'Centros Geriátricos y de Cuidado Infantil',
            'Servicios de Salud Ocupacional en empresas',
            'Atención de enfermería domiciliaria e independiente',
        ],
        'egreso': (
            'El egresado de Enfermería del ISTTE estará capacitado para'
            ' ejecutar procedimientos clínicos de enfermería con precisión,'
            ' administrar tratamientos prescritos, colaborar en equipos de'
            ' salud en emergencias y promover hábitos de vida saludables en la'
            ' población.'
        ),
    },
}


def index(request):
    latest_media = MediaItem.objects.filter(published=True)[:3]
    latest_news = Noticia.objects.filter(
        published=True, status='publicado'
    ).order_by('-published_at')[:3]
    published_careers = Carrera.objects.filter(published=True)
    homepage_career_records = list(
        published_careers.exclude(slug='ciberseguridad')
        .order_by('-featured', 'title')[:3]
    )
    cybersecurity_career = published_careers.filter(
        slug='ciberseguridad'
    ).first()
    if cybersecurity_career:
        homepage_career_records.append(cybersecurity_career)

    homepage_careers = []
    for carrera in homepage_career_records:
        homepage_careers.append({
            'title': carrera.title,
            'slug': carrera.slug,
            'image': (
                CYBERSECURITY_IMAGE
                if carrera.slug == 'ciberseguridad'
                else carrera.image.url
                if carrera.image
                else '/static/images/carreras/default.svg'
            ),
            'description': carrera.profile or carrera.description,
        })

    if not cybersecurity_career:
        cybersecurity_data = CARRERAS_DATA['ciberseguridad']
        homepage_careers.append({
            'title': cybersecurity_data['title'],
            'slug': 'ciberseguridad',
            'image': cybersecurity_data['image'],
            'description': cybersecurity_data['profile'],
        })

    return render(
        request,
        'index.html',
        {
            'latest_media': latest_media,
            'latest_news': latest_news,
            'homepage_careers': homepage_careers,
        },
    )


def autoridades(request):
    return render(request, 'autoridades.html')


def organigrama(request):
    return render(request, 'organigrama.html')


def planificacion_estrategica(request):
    return render(request, 'planificacion_estrategica.html')


def sedes_campus(request):
    return render(request, 'sedes_campus.html')


def carreras(request):
    modalidad_filtro = request.GET.get('modalidad', None)

    # Obtener todas las carreras de la base de datos
    carreras_queryset = Carrera.objects.filter(published=True).order_by('title')

    # Filtrar por modalidad si es necesario
    if modalidad_filtro:
        modalidad = modalidad_filtro.lower()
        if modalidad == 'presencial':
            carreras_queryset = carreras_queryset.filter(
                modality__icontains='Presencial'
            )
        elif modalidad == 'linea':
            carreras_queryset = carreras_queryset.filter(
                models.Q(modality__icontains='Línea')
                | models.Q(modality__icontains='Linea')
                | models.Q(modality__icontains='En Línea')
            )

    # Convertir queryset a lista de tuplas (slug, info_dict) para compatibilidad con template
    filtered_carreras = []
    for carrera in carreras_queryset:
        info = {
            'title': carrera.title,
            'image': (
                CYBERSECURITY_IMAGE
                if carrera.slug == 'ciberseguridad'
                else (
                    carrera.image.url
                    if carrera.image
                    else '/static/images/carreras/default.svg'
                )
            ),
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

    return render(
        request,
        'carreras.html',
        {
            'carreras': filtered_carreras,
            'modalidad_filtro': modalidad_filtro,
        },
    )


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
    career_slug = career_slug.lower()

    # Primero intentar buscar en la base de datos
    try:
        carrera = Carrera.objects.get(slug=career_slug, published=True)
        career_info = {
            'title': carrera.title,
            'image': (
                CYBERSECURITY_IMAGE
                if carrera.slug == 'ciberseguridad'
                else (
                    carrera.image.url
                    if carrera.image
                    else '/static/images/carreras/default.svg'
                )
            ),
            'profile_image': (
                CYBERSECURITY_IMAGE
                if carrera.slug == 'ciberseguridad'
                else (
                    carrera.profile_image.url
                    if carrera.profile_image
                    else None
                )
            ),
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
        return render(
            request,
            'detalle_carreras.html',
            {'career_slug': career_slug, 'career': career_info},
        )
    except Carrera.DoesNotExist:
        # Si no existe en la BD, buscar en CARRERAS_DATA para compatibilidad
        if career_slug in CARRERAS_DATA:
            career_info = CARRERAS_DATA[career_slug]
            return render(
                request,
                'detalle_carreras.html',
                {'career_slug': career_slug, 'career': career_info},
            )
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


# NUEVA FUNCIÓN PARA PROCESAR EL FORMULARIO DE INFORMACIÓN DEL CEC
def solicitar_informacion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cedula = request.POST.get('cedula', '')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        programa = request.POST.get('programa')

        # Muestra una notificación de éxito al usuario
        messages.success(
            request,
            f'¡Gracias {nombre}! Tu solicitud de información para {programa} ha sido registrada exitosamente.'
        )

    return redirect('cec_tecno')


def bienestar(request):
    return render(request, 'bienestar.html')


def vinculacion(request):
    return render(request, 'vinculacion.html')


def investigacion(request):
    return render(request, 'investigacion.html')


def tecno_informativo(request):
    news_items = Noticia.objects.filter(
        published=True, status='publicado'
    ).order_by('-published_at')
    return render(
        request, 'tecno_informativo.html', {'news_items': news_items}
    )


def noticia_detalle(request, slug):
    noticia = get_object_or_404(
        Noticia, slug=slug, published=True, status='publicado'
    )
    return render(request, 'noticia_detalle.html', {'noticia': noticia})


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
    media_items = MediaItem.objects.filter(published=True)
    news_items = Noticia.objects.filter(
        published=True, status='publicado'
    ).order_by('-published_at')
    return render(
        request,
        'multimedia.html',
        {
            'media_items': media_items,
            'news_items': news_items,
        },
    )


def upload_media(request):
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
