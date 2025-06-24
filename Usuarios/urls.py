from django.urls import path
from django.contrib.auth import views as auth_views
from Usuarios import views

urlpatterns = [
    path('registrarse/',views.crearUsuario, name ='inscribirse'),
    path('sesion/', views.inicioSesion, name='iniciosesion'),
    path('cerrar/', views.cerrarSesion, name='cerrarsesion'),
]
