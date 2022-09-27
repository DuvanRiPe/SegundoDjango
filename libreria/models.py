from django.db import models

# Create your models here.
# cada vez que se crea un modelo hay que hacer las migraciones con makemigrations y migrate
# en django y trabajar con migraciones no es necesario hacer las tablas en phpmyadmin, las migraciones crea esa tabla automaticamente, todo depndera de la informacxion de la clase.

class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Título")
    imagen=models.ImageField(upload_to='imagenes/',verbose_name="Imagen" ,null=True)
    descripcion=models.TextField(verbose_name="Descripción",null=True)

    # esta funcion se realiza con el fin de que en el administrador nos apresca los nombres de los titulos y la descripcion de lo que hay en la tabla 
    def __str__(self):
        fila=(f"Titulo: {self.titulo} - Descripción: {self.descripcion}")
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
