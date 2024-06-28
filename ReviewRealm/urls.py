#from django.conf.urls import urls
from django.urls import path
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
    path('juegos', views.lista_juegos, name='juegos'),
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
]