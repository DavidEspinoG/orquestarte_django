from django.db import models

# Create your models here.
class ClaseVirtual(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/')
    