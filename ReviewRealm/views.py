from django.shortcuts import render
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    context={}
    return render(request, 'ReviewRealm/index.html', context)

def categorias(request):
    context={}
    return render(request, 'ReviewRealm/categorias.html', context)

def ingresar_juego(request):
    context={}
    return render(request, 'ReviewRealm/ingresar_juego.html', context)

def inicio_sesion(request):
    context={}
    return render(request, 'ReviewRealm/inicio_sesion.html', context)

def perfil(request):
    context={}
    return render(request, 'ReviewRealm/perfil.html', context)

def recomendacion_aleatoria(request):
    context={}
    return render(request, 'ReviewRealm/recomendacion_aleatoria.html', context)

def registrarse(request):
    context={}
    return render(request, 'ReviewRealm/registrarse.html', context)


