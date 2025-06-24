from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # ← PDF 7
# Create your views here.

def crearUsuario(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:    
                usuario = User.objects.create_user(username= request.POST['username'],password= request.POST['password1'])
                usuario.save()
                login(request,usuario)
                return redirect('Inicio')
            except:
                return render(request, ('Crear_usu.html'), {'form' : UserCreationForm ,'error':' usuario ya existe'})
        else:
            return render(request, ('Crear_usu.html'), {'form' : UserCreationForm ,'error':'Contraseña no coinciden'})
    return render(request, ('Crear_usu.html'), {'form' : UserCreationForm})

def inicioSesion(request):
    if request.method == 'GET':
        return render(request,('inicia_sesion.html'),{'form': AuthenticationForm})
    else:
        usuario = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if usuario is None:
            return render(request,('inicia_sesion.html'),{'form': AuthenticationForm}) 
        else:
            login(request,usuario)
            return redirect('Inicio')

def cerrarSesion(request):
    logout(request)
    return redirect('Inicio')

