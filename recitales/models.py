from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Recital(models.Model):
    title = models.CharField(max_length=30, verbose_name="Título")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    class Meta: 
        verbose_name = "Recital"
        verbose_name_plural = "Recitales"
    def __str__(self):
        return self.title

class Participacion(models.Model):
    student = models.CharField(max_length=30, verbose_name="Alumno(a)")
    piece = models.CharField(max_length=60, verbose_name="Pieza")
    composer = models.CharField(max_length=30, verbose_name="Compositor")
    teacher = models.CharField(max_length=30, verbose_name="Maestro")
    recital = models.ForeignKey(Recital, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Participacion"
        verbose_name_plural = "Participaciones"
    def __str__(self):
        return self.student