from django.db import models

# Create your models here.

class HomeP(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    class Meta:
        verbose_name = 'Home articulo'
        verbose_name_plural = 'Home articulos'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo+' - '+self.subtitutlo