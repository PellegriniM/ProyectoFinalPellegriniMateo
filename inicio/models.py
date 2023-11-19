from django.db import models
from ckeditor.fields import RichTextField

class Noticia(models.Model):
    autor = models.CharField(max_length=30)
    asunto = models.CharField(max_length=30)
    descripcion = RichTextField()
    fecha_creacion = models.DateField()
    imagen = models.ImageField()

    def __str__(self):
        return f'{self.id} - {self.autor} {self.asunto} - {self.fecha_creacion}'