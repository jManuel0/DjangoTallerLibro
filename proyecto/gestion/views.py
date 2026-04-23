from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro
from .forms import LibroForm

# Listar todos los libros
class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/libro_list.html'
    context_object_name = 'libros'
    paginate_by = 10

# Ver detalles de un libro
class LibroDetailView(DetailView):
    model = Libro
    template_name = 'gestion/libro_detail.html'
    context_object_name = 'libro'

# Crear un nuevo libro
class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('libro-list')

# Actualizar un libro
class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('libro-list')

# Eliminar un libro
class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/libro_confirm_delete.html'
    success_url = reverse_lazy('libro-list')
