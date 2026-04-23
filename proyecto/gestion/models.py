from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    cantidad = models.IntegerField(default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.titulo
