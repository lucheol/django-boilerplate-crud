from django.urls import path
from .views import EstadoListView, EstadoCreateView, EstadoUpdateView, EstadoDeleteView, EstadoDetailView

urlpatterns = [
    path('list/', EstadoListView.as_view(), name='class_based_list'),
    path('create/', EstadoCreateView.as_view(), name='class_based_create'),
    path('update/<int:pk>/', EstadoUpdateView.as_view(), name='class_based_update'),
    path('delete/<int:pk>/', EstadoDeleteView.as_view(), name='class_based_delete'),
    path('detail/<int:pk>/', EstadoDetailView.as_view(), name='class_based_detail'),
]
