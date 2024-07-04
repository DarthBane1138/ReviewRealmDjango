from django.shortcuts import render, redirect
from ReviewRealm.models import Genero_Juego, Juego
from .forms import GeneroJuegoForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required
def menu(request):
    juegos = Juego.objects.all()
    generos_juegos = Genero_Juego.objects.all()
    context = {'juegos':juegos, 'generos_juegos':generos_juegos}
    return render(request, 'Administrador/index.html', context)

@login_required
def registro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        mensaje = None # Inicializa el mensaje como None

        if password1 != password2:
            mensaje = "Las contraseñas no coinciden."
        elif User.objects.filter(username=username).exist():
            mensaje = "El nombre de usuario ya está en uso."
        elif User.objects.filter(email=email).exist():
            mensaje = "El correo ya se encuentra registrado."
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user)
                mensaje = f"¡Cuenta creada para {username}!"
                return redirect("index") # Acá se redirigirá a la página de inicio o donde se prefiera
        
        context = {'mensaje':mensaje}
        return render(request, "registration/registro.html", context)
    
    return render(request, "registration/registro.html")

@login_required
def crud(request):
    juegos = Juego.objects.all()
    context = {'juegos': juegos}
    return render(request, 'Administrador/juegos_list.html', context)

@login_required
def juegosAdd(request):
    if request.method != "POST":
        # No es un POST, por lo tanto se muestra el formulario para agregar
        # Esta es la primera instancia, debido a que se llama al formulario, pero aún no se ha pinchado el botón agregar (El que llama a un "POST")
        generos_juegos = Genero_Juego.objects.all()
        context={'generos_juegos':generos_juegos}
        return render(request, 'Administrador/juegos_add.html', context)
    
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
        # Esta es la creación de un objeto con los datos obtenidos desde el formulario
        
        obj.save()
        context = {'mensaje':"Ok, datos grabados..."}
        return render(request, 'Administrador/juegos_add.html')

@login_required
def juegos_del(request,pk):
    context={}
    try:
        juego = Juego.objects.get(id_juego=pk)

        juego.delete()
        mensaje="Bien, datos eliminados..."
        juegos = Juego.objects.all()
        context = {'juegos':juegos, 'mensaje':mensaje}
        return render(request, 'Administrador/juegos_list.html', context)
    except:
        mensaje = "Error, el id no existe"
        juegos = Juego.objects.all()
        context = {'juegos':juegos, 'mensaje':mensaje}
        return render(request, 'Administrador/juegos_list.html', context)

@login_required
def juegos_findEdit(request, pk):

    if pk != "":
        juego = Juego.objects.get(id_juego=pk)
        generos_juegos = Genero_Juego.objects.all()

        print(type(juego.id_genero_juego.nombre_genero))

        context={'juego':juego, 'generos_juegos':generos_juegos}
        if juego:
            return render(request, 'Administrador/juegos_edit.html', context)
        else:
            context={'mensaje':"Error, id no existe..."}
            return render(request, 'Administrador/juegos_list.html', context)

@login_required        
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
        return render(request, 'Administrador/juegos_edit.html', context)
    else:
        # No es un POST, por lo tanto se muestra el formulario para agregar.
        juegos = Juego.objects.all()
        context={'juegos': juegos}
        return render(request, 'Administrador/juegos_list.html', context)
    
###################################### Géneros Juegos ######################################

@login_required
def crud_generos_juegos(request):

    generos_juegos = Genero_Juego.objects.all()
    context = {'generos_juegos': generos_juegos}
    print("Enviando datos generos_list")
    return render(request, "Administrador/generos_juegos_list.html", context)

@login_required
def generosJuegosAdd(request):
    print("Estoy en el controlador generosJuegosAdd...")
    context={}

    if request.method == "POST":
        print("El controlador es un POST...")
        form = GeneroJuegoForm(request.POST)
        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            # Limpiar form
            form = GeneroJuegoForm()

            context={'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, "Administrador/generos_juegos_add.html", context)
    else:
        form = GeneroJuegoForm()
        context = {'form':form}
        return render(request, 'Administrador/generos_juegos_add.html', context)

@login_required
def generosJuegos_del(request, pk):
    mensajes=[]
    errores=[]
    generos_juegos = Genero_Juego.objects.all()
    try:
        genero_juego = Genero_Juego.objects.get(id_genero_juego=pk)
        context={}
        if genero_juego:
            genero_juego.delete()
            mensajes.append("Bien, datos eliminados...")
            context = {'generos_juegos':generos_juegos, 'mensajes':mensajes, 'errores':errores}
            return render(request, 'Administrador/generos_juegos_list.html', context)
    except:
        print("Error,id no existe...")
        generos_juegos=Genero_Juego.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos_juegos':generos_juegos}
        return render(request, 'Administrador/generos_juegos_list.html', context)

@login_required
def generosJuegos_edit(request, pk):
    context={}
    try:
        genero_juego=Genero_Juego.objects.get(id_genero_juego=pk)
        if genero_juego:
            print("Edit encontró el género juego...")
            if request.method == "POST":
                print("edit, es un POST")
                form = GeneroJuegoForm(request.POST,instance=genero_juego)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'genero_juego':genero_juego, 'form':form, 'mensaje':mensaje}
                return render(request, 'Administrador/generos_juegos_edit.html', context)
            else:
                # No es un POST
                print("Edit, no es un POST")
                form = GeneroJuegoForm(instance=genero_juego)
                mensaje=""
                context = {'genero_juego':genero_juego, 'form':form, 'mensaje':mensaje}
                print(context)
                return render(request, 'Administrador/generos_juegos_edit.html', context)
    except:
        print("Error, id no existe...")
        generos_juegos=Genero_Juego.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos_juegos':generos_juegos}
        return render(request, 'Administrador/generos_juegos_list.html', context)
    
@login_required
def mantenedorIndex(request):
    juegos = Juego.objects.all()
    generos_juegos = Genero_Juego.objects.all()
    context={"juegos":juegos, "generos_juegos":generos_juegos}
    return render(request, 'Administrador/index_list.html', context)

@login_required
def lista_juegos(request):
    juegos= Juego.objects.all()
    context={"juegos":juegos, 'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'Administrador/lista_juegos.html', context)

@login_required
def listadoSQL(request):
    juegos= Juego.objects.raw('SELECT * FROM ReviewRealm_juego')
    print(juegos)
    context={"juegos":juegos}
    return render(request, 'Administrador/listadoSQL.html', context)