from django.db import models
from django.contrib.auth.models import User

class Almacen(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.IntegerField()

    class Meta:
     verbose_name_plural = "Almacén"

    def __str__(self):
        return f"{self.nombre}"


class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    

class Verdura (models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    unidad= models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return f"{self.nombre}"
    
class Fruta(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    unidad= models.DecimalField(max_digits=10, decimal_places=1)
    def __str__(self):
        return f"{self.nombre}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"