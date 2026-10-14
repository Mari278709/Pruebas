from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class MediaItem(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/videos/', blank=True, null=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Elemento multimedia'
        verbose_name_plural = 'Elementos multimedia'

    def __str__(self):
        return self.title


class Inscripcion(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    carrera = models.CharField(max_length=100)
    modalidad = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.carrera}"


class Carrera(models.Model):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=120, blank=True)
    modality = models.CharField(max_length=120, blank=True)
    degree = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='uploads/carreras/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='uploads/carreras/perfiles/', blank=True, null=True, verbose_name='Imagen de perfil')
    learn = models.JSONField(blank=True, null=True, default=list, verbose_name='Qué aprenderás')
    campo = models.JSONField(blank=True, null=True, default=list, verbose_name='Campo ocupacional')
    malla = models.JSONField(blank=True, null=True, default=dict, verbose_name='Malla curricular')
    egreso = models.TextField(blank=True, verbose_name='Perfil de egreso')
    video_url = models.URLField(blank=True)
    profile = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Autoridad(models.Model):
    full_name = models.CharField(max_length=220)
    position = models.CharField(max_length=220, blank=True)
    biography = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/autoridades/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'full_name']
        verbose_name = 'Autoridad'
        verbose_name_plural = 'Autoridades'

    def __str__(self):
        return self.full_name


class Sede(models.Model):
    name = models.CharField(max_length=220)
    address = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=60, blank=True)
    email = models.EmailField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/sedes/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return self.name


class Noticia(models.Model):
    ESTADO_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Autor")
    
    content = CKEditor5Field('Contenido', config_name='extends', blank=True)
    summary = models.TextField(blank=True, verbose_name="Extracto")
    image = models.ImageField(upload_to='uploads/noticias/', blank=True, null=True, verbose_name="Imagen destacada")
    
    status = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='borrador', verbose_name="Estado")
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Fecha de publicación")
    
    categorias = models.ManyToManyField(Categoria, blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def reading_time(self):
        palabras = len(self.content.split())
        minutos = max(1, round(palabras / 200)) if palabras else 1
        return f"{palabras} palabras, {minutos} min de lectura"

    def __str__(self):
        return self.title


class OportunidadLaboral(models.Model):
    title = models.CharField(max_length=220)
    company = models.CharField(max_length=220, blank=True)
    location = models.CharField(max_length=220, blank=True)
    modality = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Oportunidad laboral'
        verbose_name_plural = 'Oportunidades laborales'

    def __str__(self):
        return self.title