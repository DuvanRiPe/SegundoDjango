from django.shortcuts import render
from .models import Libro # importamos el modelo
from .forms import LibroForm


# Create your views here.
def inicio(request):
    return render(request, 'pages/inicio.html')

def nosotros(request):
    return render(request, 'pages/nosotros.html')

def libros(request):
    # en esta linea de codigo lo que hacemos es pedir todo lo que esta en el modelo Libro y lo uardamos en libros que es la variable.
    libros=Libro.objects.all()
    # colocamos {'libros':libros} donde 'libros' con comillas es la llave y libros sin comillas es el valor y esta es la variable donde guardamos la informacion que agarramos de el modelo Libro, esto para poder mostrarlo en la vista en forma de tabla.
    return render(request, 'libros/libros.html', {'libros': libros})

def crear(request):
    formulario=LibroForm(request.POST or None)
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request):
    return render(request, 'libros/editar.html')