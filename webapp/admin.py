from django.contrib import admin
from .models import (
    Autoridad,
    Carrera,
    Categoria,
    Etiqueta,
    MediaItem,
    Noticia,
    OportunidadLaboral,
    Sede,
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    search_fields = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    search_fields = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'video', 'published')
        }),
        ('Información', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('title', 'modality', 'featured', 'published', 'created_at')
    list_filter = ('published', 'featured', 'modality')
    search_fields = ('title', 'description', 'degree')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'duration', 'modality', 'degree', 'image', 'profile_image', 'video_url', 'profile')
        }),
        ('Contenido detallado', {
            'fields': ('learn', 'campo', 'malla', 'egreso'),
            'classes': ('collapse',),
        }),
        ('Opciones de publicación', {
            'fields': ('featured', 'published')
        }),
    )


@admin.register(Autoridad)
class AutoridadAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'order', 'published')
    list_filter = ('published',)
    search_fields = ('full_name', 'position', 'biography')
    ordering = ('order', 'full_name')


@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'order', 'published')
    list_filter = ('published',)
    search_fields = ('name', 'address', 'email')
    ordering = ('order', 'name')


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published', 'published_at', 'reading_time')
    list_filter = ('status', 'published', 'categorias', 'published_at')
    search_fields = ('title', 'summary', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categorias', 'etiquetas')
    readonly_fields = ('reading_time', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('title', 'slug', 'author', 'content', 'summary', 'image')
        }),
        ('Publicación y Estado', {
            'fields': ('status', 'published', 'published_at', 'reading_time')
        }),
        ('Clasificación', {
            'fields': ('categorias', 'etiquetas')
        }),
        ('Metadatos del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(OportunidadLaboral)
class OportunidadLaboralAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'modality', 'published')
    list_filter = ('published', 'modality')
    search_fields = ('title', 'company', 'description')