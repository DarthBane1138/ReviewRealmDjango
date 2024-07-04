from django import forms
from ReviewRealm.models import Genero_Juego

from django.forms import ModelForm

class GeneroJuegoForm(ModelForm):
    class Meta:
        model = Genero_Juego
        fields = ['nombre_genero']
        labels = {'nombre_genero':'Nombre género'}

# Se importa la clase Genero_Juego y esta hereda de ModelForm en la creación de la clase
# La subclase Meta se encarga de indicar en qué modelo están lo datos y que campos se mostrarán "__all__" para todos