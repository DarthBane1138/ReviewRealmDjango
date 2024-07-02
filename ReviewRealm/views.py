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

def crud(request):
    juegos = Juego.objects.all()
    context = {'juegos': juegos}
    return render(request, 'ReviewRealm/juegos_list.html', context)

def juegosAdd(request):
    if request.method != "POST":
        # No es un POST, por lo tanto se muestra el formulario para agregar
        generos_juegos = Genero_Juego.objects.all()
        context={'generos_juegos':generos_juegos}
        return render(request, 'ReviewRealm/juegos_add.html', context)
    
    else:
        # Es un POST, por lo tanto se recuperan los datos del formulario
        # y se graban en la tabla.

        #id_juego = request.POST["id_juego"]
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

        # A continuación se hace referencia a los nombres del modelo "los nombres antes del = son los mismos nombres que aparecen en models.py"
        objGenero_Juego = Genero_Juego.objects.get(id_genero_juego = nombre_genero)
        obj = Juego.objects.create( titulo = titulo,
                                    descripcion = descripcion,
                                    anio = anio,
                                    id_genero_juego = objGenero_Juego,
                                    desarrollador = desarrollador,
                                    publisher = publisher,
                                    calificacion = calificacion,
                                    plataforma = plataforma,
                                    duracion = duracion,
                                    clasificacion = clasificacion,
                                    imagen_portada = imagen_portada )
        
        obj.save()
        context = {'mensaje':"Ok, datos grabados..."}
        return render(request, 'ReviewRealm/juegos_add.html')

def juegos_del(request,pk):
    context={}
    try:
        juego = Juego.objects.get(id_juego=pk)

        juego.delete()
        mensaje="Bien, datos eliminados..."
        juegos = Juego.objects.all()
        context = {'juegos':juegos, 'mensaje':mensaje}
        return render(request, 'ReviewRealm/juegos_list.html', context)
    except:
        mensaje = "Error, el id no existe"
        juegos = Juego.objects.all()
        context = {'juegos':juegos, 'mensaje':mensaje}
        return render(request, 'ReviewRealm/juegos_list.html', context)

def juegos_findEdit(request, pk):

    if pk != "":
        juego = Juego.objects.get(id_juego=pk)
        generos_juegos = Genero_Juego.objects.all()

        print(type(juego.id_genero_juego.nombre_genero))

        context={'juego':juego, 'generos_juegos':generos_juegos}
        if juego:
            return render(request, 'ReviewRealm/juegos_edit.html', context)
        else:
            context={'mensaje':"Error, id no existe..."}
            return render(request, 'ReviewRealm/juegos_list.html', context)
        
def juegosUpdate(request):
    if request.method == "POST":
        # Es un POST, por lo tanto se recuperan los datos del formulario u se graban en la tabla.
        id_juego = request.POST["id_juego"]
        titulo = request.POST["titulo"]
        descripcion = request.POST["descripcion"]
        anio = request.POST["anio"]
        nombre_genero = request.POST["nombre_genero"]
        desarrollador = request.POST["desarrollador"]
        publisher = request.POST["publisher"]
        plataforma = request.POST["plataforma"]
        duracion = request.POST["duracion"]
        calificacion = request.POST["calificacion"]
        clasificacion = request.POST["clasificacion"]
        imagen_portada = request.FILES.get("nueva_portada")

        # A continuación se hace referencia a los nombres del modelo "los nombres antes del = son los mismos nombres que aparecen en models.py"
        objGenero_Juego = Genero_Juego.objects.get(id_genero_juego= nombre_genero)

        id_juego = request.POST.get("id_juego")
        if id_juego:
            juego = Juego.objects.get(pk=id_juego)
        else:
            juego = Juego()

        juego = Juego()
        juego.id_juego = id_juego
        juego.titulo = titulo
        juego.descripcion = descripcion
        juego.anio = anio
        juego.id_genero_juego = objGenero_Juego
        juego.desarrollador = desarrollador
        juego.publisher = publisher
        juego.plataforma = plataforma
        juego.duracion = duracion
        juego.calificacion = calificacion
        juego.clasificacion = clasificacion
        juego.imagen_portada = imagen_portada
        if imagen_portada:
            juego.imagen_portada = imagen_portada
        elif id_juego and not imagen_portada:
            # Si es una actualización y no se carga una nueva imagen, mantener la imagen existente
            juego.imagen_portada = Juego.objects.get(pk=id_juego).imagen_portada

        juego.save()

        #nueva_imagen = input("Ingrese la nueva imagen: ")

        #    if nueva_imagen:
        #        # Si se carga una imagen, asigna su valor a nueva_portada
        #        nueva_portada = nueva_imagen
        #    else:
        #        # Si no se carga nada, no se guarda ningún valor en nueva_portada
        #        nueva_portada = None

# Luego puedes usar nueva_portada en tu formulario
        
        generos_juegos = Genero_Juego.objects.all()
        context={'mensaje':"Ok, datos actualizados...", 'generos_juegos':generos_juegos, 'juego':juego}
        return render(request, 'ReviewRealm/juegos_edit.html', context)
    else:
        # No es un POST, por lo tanto se muestra el formulario para agregar.
        juegos = Juego.objects.all()
        context={'juegos': juegos}
        return render(request, 'ReviewRealm/juegos_list.html', context)


