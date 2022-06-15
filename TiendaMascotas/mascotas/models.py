from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria=models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self): 
        return self.nombreCategoria


class Cliente (models.Model): 
    rut = models.CharField(primary_key=True, max_length=9, verbose_name='Rut')
    nombre= models.CharField(max_length=70, verbose_name='Nombre')
    correo= models.CharField(max_length=50, verbose_name='Correo')
    celular= models.CharField(max_length=13, verbose_name='Celular')
    direccion= models.CharField(max_length=50, verbose_name='Direccion')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.rut

class Producto (models.Model): 
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombre= models.CharField(max_length=20, verbose_name='Nombre')
    precio= models.CharField(max_length=6, verbose_name='Precio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    foto = models.ImageField(upload_to = "images/",null=True,blank=True)

    def __str__(self):
        return self.nombre