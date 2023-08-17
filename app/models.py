from django.db import models

# Create your models here.
class Pieza(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits = 10, decimal_places=2)
    dimensiones = models.CharField(max_length=100)
    tecnica = models.CharField(max_length=100)

class Comprador(models.Model):
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.DecimalField(max_digits = 13, decimal_places=0)


class Vendedor(models.Model):
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.DecimalField(max_digits = 13, decimal_places=0)



