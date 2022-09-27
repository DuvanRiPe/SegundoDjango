from django.contrib import admin

#aqui lo que hacemos es importar el modelo creado que en este caso es libro, esto viene de model.py
from .models import Libro 

#estos registros se hace para que el administrador tenga manipulacion sobre LIbro que es el modelo creado
admin.site.register(Libro) 