from django.urls import path
from .views import *

urlpatterns=[
    path('Productos/listar/',listar_productos, name='listar_productos'),
    path('Productos/agregar/',agregar_productos, name='agregar_productos'),
    path('Productos/editar/<int:idproducto>/',modificar_productos, name='modificar_productos'),
    path('Productos/eliminar/<int:idproducto>/',eliminar_productos, name='eliminar_productos'),
]