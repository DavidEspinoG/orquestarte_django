from tabnanny import verbose
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