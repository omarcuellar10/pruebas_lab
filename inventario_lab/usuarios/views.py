
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
#from .models import Producto, Ubicacion  # Asumiendo que tienes estos modelos

def stock_ubicaciones(request):
    productos = Producto.objects.all()
    ubicaciones = Ubicacion.objects.all()
    context = {
        'productos': productos,
        'ubicaciones': ubicaciones,
    }
    return render(request, 'stock_ubicaciones.html', context)

@login_required
def dashboard_view(request):
    return render(request, 'usuarios/dashboard.html', {
        'usuario': request.user
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  
        if user:
            login(request, user)
            return redirect('dashboard')  # Cambia esto según tu vista principal
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')


@login_required
def placeholder_view(request):
    return HttpResponse("Página en construcción")





def placeholder_view(request):
    return HttpResponse("Página en construcción")
