from django.db import models

# Create your models here.
class company(models.Model):
    nombre = models.CharField(max_length=50)
    sitioWeb = models.URLField(max_length=100)
    fondacion = models.PositiveBigIntegerField()
