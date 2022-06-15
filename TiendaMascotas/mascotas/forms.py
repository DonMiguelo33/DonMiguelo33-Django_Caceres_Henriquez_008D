from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Cliente, Producto


class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'correo', 'celular', 'direccion', 'categoria']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'correo': 'Correo',
            'celular': 'Celular',
            'direccion': 'Direccion',
            'categoria': 'Categoría',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nombre'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo', 
                    'id': 'correo'
                }
            ),
            'celular': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Celular', 
                    'id': 'celular'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Direccion', 
                    'id': 'direccion'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idProducto', 'nombre', 'precio', 'categoria','foto']
        labels ={
            'idProducto': 'Id del Producto', 
            'nombre': 'Nombre', 
            'precio': 'Precio', 
            'categoria': 'Categoría',
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id del Producto', 
                    'id': 'idProducto'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nombre'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Precio', 
                    'id': 'precio'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }