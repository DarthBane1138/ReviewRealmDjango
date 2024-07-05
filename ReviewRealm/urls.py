#from django.conf.urls import urls
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('categorias', views.categorias, name='categorias'),
    path('ingresar_juego', views.ingresar_juego, name='ingresar_juego'),
    path('inicio_sesion', views.inicio_sesion, name='inicio_sesion'),
    path('perfil', views.perfil, name='perfil'),
    path('recomendacion_aleatoria', views.recomendacion_aleatoria, name='recomendacion_aleatoria'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('Administrador/', include('Administrador.urls')), # Se incluyen las URLs de la aplicación Administrador
    path('juegos_por_genero/<int:pk>', views.juegos_por_genero, name='juegos_por_genero'),
    path('juego/<int:pk>', views.juego, name='juego'),
]