from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView

from .forms import LibroForm
from .models import Libro


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
