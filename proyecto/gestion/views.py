from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LibroForm
from .models import Libro


def home(request):
    return render(request, 'gestion/home.html')


def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente.')
            return redirect('libro-list')
    else:
        form = LibroForm()

    return render(request, 'gestion/libro_form.html', {'form': form})


def libro_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'gestion/libro_detail.html', {'libro': libro})


class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/libro_list.html'
    context_object_name = 'libros'
    paginate_by = 5


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/libro_confirm_delete.html'
    context_object_name = 'libro'
    success_url = reverse_lazy('libro-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Libro eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Funciones basadas en vistas para operaciones CRUD- dev Developer2

def actualizar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente.')
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'gestion/funciones/libro_actualizar.html', {'form': form, 'libro': libro})


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente.')
        return redirect('lista_libros')

    return render(request, 'gestion/funciones/libro_eliminar.html', {'libro': libro})

# Vistas basadas en clases para operaciones CRUD - dev Developer2
class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/genericas/libro_update.html'
    success_url = reverse_lazy('lista_libros')


class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/genericas/libro_create.html'
    success_url = reverse_lazy('lista_libros')
