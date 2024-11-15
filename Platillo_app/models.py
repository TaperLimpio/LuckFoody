from django.db import models
from Sucursal_app.models import Sucursal
from Catalogo_app.models import Catalogo

class Platillo(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=13,default=1)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='platillo_imagenes/')
    sucursales = models.ManyToManyField(Sucursal, through='PlatilloSucursal')
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name='platillos_set')
    estado = models.CharField(max_length=20, default='Desactivado')

class PlatilloSucursal(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    platillo = models.ForeignKey('Platillo_app.Platillo', on_delete=models.CASCADE)
    disponibilidad = models.BooleanField(default=True)