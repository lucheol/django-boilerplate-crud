from django.shortcuts import render, redirect, get_object_or_404
from .models import Estado
from .forms import EstadoForm
# Create your views here.


def EstadoListView(request):

    q = Estado.objects.all()

    context = {
        'Estados': q
    }

    return render(request, 'view_based/estado_list.html', context)


def EstadoCreateView(request):

    if request.POST:

        form = EstadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('view_based_list')

        return render(request, 'view_based/estado_create.html', {'form': form})

    form = EstadoForm()

    context = {
        'form': form
    }

    return render(request, 'view_based/estado_create.html', context)


def EstadoUpdateView(request, pk):

    q = get_object_or_404(Estado, pk=pk)

    form = EstadoForm(request.POST or None, instance=q)

    if form.is_valid():
        form.save()
        return redirect('view_based_list')

    context = {
        'form': form
    }

    return render(request, 'view_based/estado_update.html', context)


def EstadoDeleteView(request, pk):

    # exemplificando a partir do GET direto

    q = get_object_or_404(Estado, pk=pk)
    q.delete()

    return redirect('view_based_list')


def EstadoDetailView(request, pk):

    # exemplificando a partir do GET direto

    q = get_object_or_404(Estado, pk=pk)

    context = {
        'Estado': q
    }

    return render(request, 'view_based/estado_detail.html', context)


def EstadoSearchView(request):

    q = None  # por padrão, não retorna nada

    if request.POST:
        NomeEstado = request.POST['NomeEstado']
        q = Estado.objects.filter(NomeEstado__icontains=NomeEstado)

    context = {
        'Estados': q
    }

    return render(request, 'view_based/estado_search.html', context)
