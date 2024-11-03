from django.db import models
from Sucursal_app.models import Sucursal
from Catalogo_app.models import Catalogo

class Platillo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='platillo_imagenes/')
    sucursales = models.ManyToManyField(Sucursal, through='PlatilloSucursal')
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name='platillos_set')

class PlatilloSucursal(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    platillo = models.ForeignKey('Platillo_app.Platillo', on_delete=models.CASCADE)
    disponibilidad = models.BooleanField(default=True)