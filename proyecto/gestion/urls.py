from django.urls import path

from .views import LibroDeleteView, LibroListView, libro_create, libro_detail

urlpatterns = [
    path('', LibroListView.as_view(), name='libro-list'),
    path('create/', libro_create, name='libro-create'),
    path('<int:pk>/', libro_detail, name='libro-detail'),
    path('<int:pk>/delete/', LibroDeleteView.as_view(), name='libro-delete'),
]
