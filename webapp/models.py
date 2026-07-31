from django.db import models


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
