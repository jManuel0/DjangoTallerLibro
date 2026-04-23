from django.urls import path

from . import views
from .views import (
    LibroCreateView,
    LibroDeleteView,
    LibroListView,
    LibroUpdateView,
    libro_create,
    libro_detail,
)

urlpatterns = [
    path('', LibroListView.as_view(), name='libro-list'),
    path('create/', libro_create, name='libro-create'),
    path('<int:pk>/', libro_detail, name='libro-detail'),
    path('<int:pk>/delete/', LibroDeleteView.as_view(), name='libro-delete'),
    path('', LibroListView.as_view(), name='lista_libros'),
    path('actualizar/<int:pk>/', views.actualizar_libro, name='actualizar_libro'),
    path('eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
    path('update/<int:pk>/', LibroUpdateView.as_view(), name='update_libro'),
    path('create/generica/', LibroCreateView.as_view(), name='create_libro'),
]
