from django.urls import path
from .views import (
    LibroListView,
    LibroDetailView,
    LibroCreateView,
    LibroUpdateView,
    LibroDeleteView
)

urlpatterns = [
    path('', LibroListView.as_view(), name='libro-list'),
    path('<int:pk>/', LibroDetailView.as_view(), name='libro-detail'),
    path('create/', LibroCreateView.as_view(), name='libro-create'),
    path('<int:pk>/update/', LibroUpdateView.as_view(), name='libro-update'),
    path('<int:pk>/delete/', LibroDeleteView.as_view(), name='libro-delete'),
]
