from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, unique=True)
    cantidad = models.IntegerField(default=0)
    ubicacion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
