from django.db import models
from django.utils import timezone
from Usuario_app.models import Usuario

# Create your models here.
class Trivia(models.Model):
    usuarioCreador = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name="Trivias_Creadas")
    usuarioRealizados= models.ManyToManyField(Usuario,related_name="Mis_trivias")
    estado = models.CharField(max_length=25)
    fechaCreacion = models.DateTimeField(default=timezone.now)
    fechaTermino = models.DateTimeField()
    descuentoofrecido = models.FloatField(default=0.0)
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField()

class Pregunta(models.Model):
    id_trivia = models.ForeignKey(Trivia,on_delete=models.CASCADE,related_name="Preguntas")
    nOrden = models.IntegerField()
    descripcion = models.TextField()

class Respuesta(models.Model):
    id_pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE,related_name="Respuestas")
    descripcion = models.TextField()
    escorrecto = models.BooleanField(default= False)
    seleccionado = models.BooleanField(default= False)

class Descuentos(models.Model):
    id_trivia = models.ForeignKey(Trivia,on_delete=models.CASCADE,related_name="descuento")
    usuPropietario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="descuentos")
    fechaCreacion = models.DateTimeField(default=timezone.now)
    fechaTermino = models.DateTimeField()
    valor = models.FloatField(default=0.0)
    porcentajeCorrecto = models.FloatField(default=0.0)
    estado = models.CharField(max_length=25,default="invalido")
