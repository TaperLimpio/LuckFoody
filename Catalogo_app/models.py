from django.db import models

class Catalogo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='catalogo_imagenes/')
    estado = models.CharField(max_length=20, default='Desactivado')

    def __str__(self):
        return self.nombre
