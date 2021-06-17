from django.db import models

# Create your models here.

class HomeP(models.Model):
    titulo = models.CharField(max_length=60)
    subtitutlo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo