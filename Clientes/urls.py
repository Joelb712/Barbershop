from django.urls import path
from Clientes import views

urlpatterns = [
    path('clientes/',views.lista_cliente, name ='Lista_Cliente'),
    path('registrar/',views.agregar_cliente, name ='Agregar_Cliente'),
    path('modificar/<int:pk>',views.modificar_cliente, name ='Modificar_Cliente'),
    path('eliminar/<int:pk>',views.eliminar_cliente, name ='Eliminar_Cliente'),
]