from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 500)

    def __str__(self):
        return self.nombre

class Marca (models.Model):
    nombre = models.CharField(max_length= 100)

    def __str__ (self):
        return self.nombre
    
class Producto (models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    categorias = models.ManyToManyField(Categoria, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to ='productos/', null=True, blank=True) #foto opcional

    def __str__ (self):
        return self.nombre
    
class Perfil (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles', null=True, blank=True)
    nombre = models.CharField(max_length= 100)

    def __str__ (self):
        return self.user.username