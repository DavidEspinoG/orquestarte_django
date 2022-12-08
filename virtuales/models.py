from django.db import models

class ClaseVirtual(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='virtuales')
    
    class Meta: 
        verbose_name = "clase virtual"
        verbose_name_plural = "clases virtuales"
    def __str__(self):
        return self.title 
