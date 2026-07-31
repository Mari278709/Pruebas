from django import forms
from .models import MediaItem


class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ['title', 'description', 'image', 'video', 'published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del contenido'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción breve del contenido'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control form-control-sm',
                'accept': 'image/*'
            }),
            'video': forms.ClearableFileInput(attrs={
                'class': 'form-control form-control-sm',
                'accept': 'video/*'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')
        if not image and not video:
            raise forms.ValidationError('Debes subir al menos una imagen o un video.')
        return cleaned_data
