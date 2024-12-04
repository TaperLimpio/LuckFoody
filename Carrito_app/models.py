from django.db import models
from Platillo_app.models import Platillo
from Usuario_app.models import Usuario

# Create your models here.
# Creacion Modelo Carrito
class Carrito(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="carrito")
    id_platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE,related_name="en_carrito")
    cantidad = models.IntegerField()
    precio = models.IntegerField()
