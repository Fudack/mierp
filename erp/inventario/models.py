from django.db import models

# Create your models here.

class productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='productos', null=True)
    ubicacion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    fechaLlegada = models.DateField(auto_now_add=True)
    fechaSalida = models.DateField(auto_now_add=True)
    stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
