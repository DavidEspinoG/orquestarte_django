from django.db import models

# Create your models here.
class Pedido(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self): 
        return self.title
        