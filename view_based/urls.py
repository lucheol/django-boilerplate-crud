from django.urls import path
from .views import (EstadoListView, EstadoCreateView,
                    EstadoUpdateView, EstadoDeleteView, EstadoDetailView, EstadoSearchView)

urlpatterns = [
    path('list/', EstadoListView, name='view_based_list'),
    path('create/', EstadoCreateView, name='view_based_create'),
    path('update/<int:pk>/', EstadoUpdateView, name='view_based_update'),
    path('delete/<int:pk>/', EstadoDeleteView, name='view_based_delete'),
    path('detail/<int:pk>/', EstadoDetailView, name='view_based_detail'),
    path('search/', EstadoSearchView, name='view_based_search'),
]
