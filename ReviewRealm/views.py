from django.shortcuts import render
from .models import Genero_Juego, Juego
from django.conf import settings

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

def lista_juegos(request):
    juegos= Juego.objects.all()
    context={"juegos":juegos,
             'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'ReviewRealm/lista_juegos.html', context)

def listadoSQL(request):
    juegos= Juego.objects.raw('SELECT * FROM ReviewRealm_juego')
    print(juegos)
    context={"juegos":juegos}
    return render(request, 'ReviewRealm/listadoSQL.html', context)