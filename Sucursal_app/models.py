from django.db import models

# Create your models here.
class Sucursal(models.Model):
        nombre=models.CharField(max_length=50)
        direccion=models.CharField(max_length=70)
        fono=models.CharField(max_length=15)
        imagen = models.ImageField(upload_to='sucursal_imagenes/',default="200x200.png")
        estado = models.CharField(max_length=20, default='activo')
        def __str__(self): 
                return self.nombre