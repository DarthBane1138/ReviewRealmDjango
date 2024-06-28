# Generated by Django 5.0.6 on 2024-06-14 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewRealm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('generos', models.CharField(blank=True, max_length=100, null=True)),
                ('id_genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='ReviewRealm.genero')),
            ],
        ),
    ]