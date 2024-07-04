#from django.conf.urls import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu', views.menu, name='menu'),

    path('crud', views.crud, name='crud'),
    path('juegosAdd', views.juegosAdd, name='juegosAdd'),
    path('juegos_del/<str:pk>', views.juegos_del, name = 'juegos_del'),
    path('juegos_findEdit/<str:pk>', views.juegos_findEdit, name = 'juegos_findEdit'),
    path('juegosUpdate', views.juegosUpdate, name='juegosUpdate'),

    path('crud_generos_juegos', views.crud_generos_juegos, name = 'crud_generos_juegos'),
    path('generosJuegosAdd', views.generosJuegosAdd, name = 'generosJuegosAdd'),
    path('generosJuegos_del/<str:pk>', views.generosJuegos_del, name = 'generosJuegos_del'),
    path('generosJuegos_edit/<str:pk>', views.generosJuegos_edit, name = 'generosJuegos_edit'),

    path('registro', views.registro, name='registro'),
]