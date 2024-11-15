from django.db import models

# Create your models here.
class Usuario(models.Model):
        rut=models.CharField(max_length=15,default='NOTRUT')
        nombre=models.CharField(max_length=50)
        email=models.CharField(max_length=60)
        fono=models.CharField(max_length=15)
        tipo=models.CharField(max_length=50)
        contraseña=models.CharField(max_length=50)
        estado = models.CharField(max_length=25)