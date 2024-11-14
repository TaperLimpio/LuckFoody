from django.db import models
from django.utils import timezone
from Usuario_app.models import Usuario
from Platillo_app.models import Platillo

# Create your models here.
class Pedido(models.Model):
    fechainicio = models.DateTimeField(default=timezone.now)
    fechaentrega = models.DateTimeField()
    direccion = models.CharField(max_length=40)
    descuento = models.FloatField()
    estado = models.CharField(max_length=25)
    repartidor = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name="pedidos_tomados")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name="pedidos_realizados")
    platillo = models.ManyToManyField(Platillo,through="lista_de_pedidos",related_name="pedidos")
    total = models.IntegerField()

class lista_de_pedidos(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()