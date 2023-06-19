# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Despensa
from .forms import DespensaForm
from django.views.decorators.http import require_safe, require_POST, require_http_methods



@require_safe
def despensa_form(request):
    rendered_page = render(request, 'despensa/form.html', {"form": DespensaForm()})
    return HttpResponse(rendered_page)

@require_safe
def despensa_list(request):
    despensas = Despensa.objects.all()

    rendered_page = render(request, 'despensa/list.html', {'despensas': despensas})

    return HttpResponse(rendered_page)


@require_safe
def despensa_detail(request, pk):
    despensa = get_object_or_404(Despensa, pk=pk)

    rendered_page = render(request, 'despensa/detail.html', {'despensa': despensa})

    return HttpResponse(rendered_page)

@require_POST
def despensa_create(request):
    nome = request.POST.get('nome')
    quantTotal = request.POST.get('quantTotal')
    capacidade = request.POST.get('capacidade')
    categoria = request.POST.get('categoria')
    Despensa.objects.create(nome=nome, quantTotal=quantTotal, capacidade=capacidade, categoria=categoria)
    return redirect('despensas:despensa_list')
    


@require_safe
def despensa_update(request, id):
    despensa = Despensa.objects.get(id=id)

    rendered_page = render(request, 'despensa/update.html', {'form': DespensaForm(), 'despensa': despensa})
    return HttpResponse(rendered_page)

@require_POST
def update(request, id):

    form = DespensaForm(request.POST)
    despensa = Despensa.objects.get(id=id)

    if form.is_valid():
        cleaned_data = form.cleaned_data

        nome = cleaned_data.get('nome')
        quantTotal = cleaned_data.get('quantTotal')
        capacidade = cleaned_data.get('capacidade')
        categoria = cleaned_data.get('categoria')

        despensa.nome = nome
        despensa.quantTotal = quantTotal
        despensa.capacidade = capacidade
        despensa.categoria = categoria
        despensa.save()

        return redirect('despensas:despensa_list')
    else:

        rendered_page = render(request, 'despensa/update.html', {'form': DespensaForm(), 'despensa': despensa})
        return HttpResponse(rendered_page)

@require_safe
def despensa_delete(request, id):
    despensa = Despensa.objects.get(id=id)
    despensa.delete()
    return redirect('despensas:despensa_list')
