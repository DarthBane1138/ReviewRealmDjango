from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
    
class Genero_Juego(models.Model):
    id_genero_juego = models.AutoField(db_column='idGeneroJuego', primary_key=True)
    nombre_genero = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_genero)

class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    anio = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(9999)])
    id_genero_juego = models.ForeignKey('Genero_Juego', on_delete=models.CASCADE, db_column='idGeneroJuego')
    desarrollador = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    plataforma = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    clasificacion = models.CharField(max_length=200)
    imagen_portada = models.ImageField(upload_to='media/portadas/', blank=True, null=True)

    # Tuve que hace una instalación en python para poder usar imágenes (python -m pip install Pillow)

    def __str__(self):
        return self.titulo