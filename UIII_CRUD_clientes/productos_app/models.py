from django.db import models

class Producto(models.Model):
    idproducto = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.IntegerField() 
    categoria = models.CharField(max_length=100)
    fecha_agregado = models.DateField()

    def __str__(self):
        return self.nombre
