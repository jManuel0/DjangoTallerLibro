from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'cantidad', 'fecha_publicacion')
    list_filter = ('fecha_publicacion', 'fecha_creacion')
    search_fields = ('titulo', 'autor', 'isbn')
    ordering = ('-fecha_creacion',)
