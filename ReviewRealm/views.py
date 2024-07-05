from django.shortcuts import render
from django.conf import settings
from Administrador.views import *
from .models import Genero_Juego, Juego

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    context={}
    return render(request, 'ReviewRealm/index.html', context)

def categorias(request):
    generos_juegos = Genero_Juego.objects.all()
    context={'generos_juegos':generos_juegos}
    # Se cuentan cuantos juegos hay para cada género
    for x in generos_juegos:
        x.cantidad_juegos = Juego.objects.filter(id_genero_juego=x).count()
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
    juegos = Juego.objects.all()
    generos_juegos = Genero_Juego.objects.all()
    context = {'juegos':juegos, 'generos_juegos':generos_juegos}
    return render(request, 'ReviewRealm/recomendacion_aleatoria.html', context)

def registrarse(request):
    context={}
    return render(request, 'ReviewRealm/registrarse.html', context)

def juegos_por_genero(request, pk):
    generos_juegos = Genero_Juego.objects.get(id_genero_juego=pk)
    juegos = Juego.objects.filter(id_genero_juego=pk)
    context = {'generos_juegos':generos_juegos, 'juegos':juegos}
    return render(request, 'ReviewRealm/juegos_por_genero.html', context)

def juego(request, pk):
    juego = Juego.objects.filter(id_juego=pk)
    context = {'juego':juego}
    print("Se encontró un juego")
    return render(request, 'ReviewRealm/juego.html', context)

