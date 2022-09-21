from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'libros/index.html')
    
def crear(request):
    return render(request, 'libros/crear.html')

def crear(request):
    return render(request, 'libros/editar.html')