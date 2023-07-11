from django.shortcuts import render, redirect
from django.http import HttpResponse
from item.models import Item
from categoria.models import Categoria
from despensa.models import Despensa
from .forms import ItemForm
from django.views.decorators.http import require_safe, require_POST


@require_safe
def item_home(request):

    rendered_page = render(request, "items/index.html", {'form': ItemForm()})

    return HttpResponse(rendered_page)

@require_POST
def save_item(request):
    nome = request.POST.get('nome')
    categoria_id = request.POST.get('categoria')
    despensa_id = request.POST.get('despensa')
    marca = request.POST.get('marca')
    peso = request.POST.get('peso')
    data_validade = request.POST.get('data_validade')


    categoria = Categoria.objects.get(id=categoria_id)
    despensa = Despensa.objects.get(id=despensa_id)

    Item.objects.create(nome=nome,
                        categoria=categoria,
                        marca=marca,
                        peso=peso,
                        data_validade=data_validade,
                        despensa=despensa)
    #rendered_page = render(request, 'items/index.html', {'form': ItemForm()})
    return redirect('items:items')

@require_safe
def list_items(request):
    items = Item.objects.all()

    rendered_page = render(request, "items/items.html", {"items": items, 'form': ItemForm()})
    return HttpResponse(rendered_page)

@require_safe
def update_item(request, id):
    item = Item.objects.get(id=id)

    rendered_page = render(request, "items/update.html", {"item": item, 'form': ItemForm()})
    return HttpResponse(rendered_page)

@require_POST
def update(request, id):
    nome = request.POST.get('nome')
    categoria_id = request.POST.get('categoria')
    despensa_id = request.POST.get('despensa')
    marca = request.POST.get('marca')
    peso = request.POST.get('peso')
    data_validade = request.POST.get('data_validade')

    categoria = Categoria.objects.get(id=categoria_id)
    despensa = Despensa.objects.get(id=despensa_id)

    item = Item.objects.get(id=id)
    item.nome = nome
    item.categoria = categoria
    item.despensa = despensa
    item.marca = marca
    item.peso = peso
    item.data_validade = data_validade
    item.save()

    return redirect('items:items')

@require_safe
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('items:items')

@require_POST
def search_items(request):
    s_nome = request.POST.get('search')
    if s_nome:
        items = Item.objects.filter(nome__icontains=s_nome)

        rendered_page = render(request, "items/search.html", {"items": items})
        return HttpResponse(rendered_page)
    else:
        items = ""
        rendered_page = render(request, "items/search.html", {"items": items})
        return HttpResponse(rendered_page)
