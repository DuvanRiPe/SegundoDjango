from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'pages/inicio.html')

def nosotros(request):
    return render(request, 'pages/nosotros.html')

def libros(request):
    return render(request, 'libros/libros.html')

def crear(request):
    return render(request, 'libros/crear.html')

def editar(request):
    return render(request, 'libros/editar.html')