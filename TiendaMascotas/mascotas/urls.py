from django.urls import path
from .views import home, catalogo, quienes_somos, registro, api, mostrar, form_cliente, form_mod_cliente, form_del_cliente, mostrar2, form_producto, form_mod_producto, form_del_producto

urlpatterns = [
    path('', home, name="home"),
    path('catalogo/', catalogo, name="catalogo"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('registro/', registro, name="registro"),
    path('api/', api, name="api"),
    path('form_cliente/', form_cliente, name="form_cliente"),
    path('mostrar/', mostrar, name="mostrar"),
    path('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path('form_producto/', form_producto, name="form_producto"),
    path('mostrar2/', mostrar2, name="mostrar2"),
    path('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
]