from django.shortcuts import render
from django.conf import settings
from Administrador.views import *
from .models import Genero_Juego, Juego

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

# Vista index
def index(request):
    context={}
    return render(request, 'ReviewRealm/index.html', context)

# Vista Categorías
def categorias(request):
    generos_juegos = Genero_Juego.objects.all()
    context={'generos_juegos':generos_juegos}
    # Se cuentan cuantos juegos hay para cada género
    for x in generos_juegos:
        x.cantidad_juegos = Juego.objects.filter(id_genero_juego=x).count()
    return render(request, 'ReviewRealm/categorias.html', context)

# Vista para buscar juegos por id
def buscar_juego(request):
    query = request.GET.get('q')
    results = []
    if query:
        # Búsqueda por título
        results = Juego.objects.filter(titulo__icontains=query)
        # Búsqueda por año (conversión de query a entero)
        try:
            query_int = int(query)
            results = Juego.objects.filter(anio=query_int)
        except ValueError:
            pass
    context = {"results": results, "query": query}
    return render(request, 'ReviewRealm/buscar_juego.html', context)
    


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

@login_required
def agregar_juego(request):
    if request.method != "POST":
        generos_juegos = Genero_Juego.objects.all()
        context = {'generos_juegos':generos_juegos}
        return render(request, 'ReviewRealm/agregar_juego.html', context)
    
    else:
        titulo = request.POST["titulo"]
        # Validación de que no existe el juego (Por título)
        if Juego.objects.filter(titulo=titulo).exists():
            generos_juegos = Genero_Juego.objects.all()
            context = {'genero_juegos':generos_juegos, 'mensaje': "Ya existe un juego con este título"}
            return render(request, 'ReviewRealm/agregar_juego.html', context)

        titulo          = request.POST["titulo"]
        descripcion     = request.POST["descripcion"]
        anio            = request.POST["anio"]
        nombre_genero   = request.POST["nombre_genero"]
        desarrollador   = request.POST["desarrollador"]
        publisher       = request.POST["publisher"]
        calificacion    = request.POST["calificacion"]
        plataforma      = request.POST["plataforma"]
        duracion        = request.POST["duracion"]
        clasificacion   = request.POST["clasificacion"]
        imagen_portada  = request.FILES.get("imagen_portada")

        objGenero_Juego = Genero_Juego.objects.get(id_genero_juego = nombre_genero)
        obj = Juego.objects.create (
            titulo          = titulo,
            descripcion     = descripcion,
            anio            = anio,
            id_genero_juego = objGenero_Juego,
            desarrollador   = desarrollador,
            publisher       = publisher,
            calificacion    = calificacion,
            plataforma      = plataforma,
            duracion        = duracion,
            clasificacion   = clasificacion,
            imagen_portada  = imagen_portada
        )

        obj.save()

        generos_juegos = Genero_Juego.objects.all()
        context = {'generos_juegos': generos_juegos, 'mensaje': "El juego ha sido ingresado exitosamente"}
        return render(request, 'ReviewRealm/agregar_juego.html', context)

