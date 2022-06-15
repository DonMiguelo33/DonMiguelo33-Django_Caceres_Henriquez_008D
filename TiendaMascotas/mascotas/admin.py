from django.contrib import admin
from .models import Categoria, Cliente, Producto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Producto)