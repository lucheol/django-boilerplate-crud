from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Estado
# Create your views here.


class EstadoListView(ListView):
    model = Estado
    template_name = "class_based/estado_list.html"
    context_object_name = 'Estados'


class EstadoCreateView(CreateView):
    model = Estado
    template_name = "class_based/estado_create.html"
    fields = '__all__'
    success_url = reverse_lazy('class_based_list')


class EstadoUpdateView(UpdateView):
    model = Estado
    template_name = "class_based/estado_update.html"
    fields = '__all__'
    success_url = reverse_lazy('class_based_list')


class EstadoDeleteView(DeleteView):
    model = Estado
    template_name = "class_based/estado_delete.html"
    success_url = reverse_lazy('class_based_list')
    context_object_name = 'Estado'


class EstadoDetailView(DetailView):
    model = Estado
    template_name = "class_based/estado_detail.html"
    context_object_name = 'Estado'
