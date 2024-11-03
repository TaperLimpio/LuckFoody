from django.db import models

class Catalogo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='catalogo_imagenes/')

