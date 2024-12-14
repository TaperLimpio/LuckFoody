from django.db import models

# Create your models here.
#modelo de usuario
class Usuario(models.Model):
        rut=models.CharField(max_length=15,default='NOTRUT')
        nombre=models.CharField(max_length=50)
        email=models.CharField(max_length=60)
        fono=models.CharField(max_length=15)
        tipo=models.CharField(max_length=50)
        contraseña=models.CharField(max_length=76)
        estado = models.CharField(max_length=25)
        ciudad=models.CharField(max_length=20,default="osorno")