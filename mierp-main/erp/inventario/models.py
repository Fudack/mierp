from django.db import models

# Create your models here.

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    fechaLlegada = models.DateField(auto_now_add=True)
    stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
