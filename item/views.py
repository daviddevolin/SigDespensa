from django.shortcuts import render, redirect
from django.http import HttpResponse
from item.models import Item
from .forms import ItemForm
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def item_home(request):

    rendered_page = render(request, "items/index.html", {'form': ItemForm()})

    return HttpResponse(rendered_page)

@require_http_methods(["GET", "POST"])
def save_item(request):
    nome = request.POST.get('nome')
    categoria = request.POST.get('categoria')
    marca = request.POST.get('marca')
    peso = request.POST.get('peso')
    data_validade = request.POST.get('data_validade')

    Item.objects.create(nome=nome,
                        categoria=categoria,
                        marca=marca,
                        peso=peso,
                        data_validade=data_validade)
    rendered_page = render(request, 'items/index.html', {'form': ItemForm()})
    return HttpResponse(rendered_page)

@require_http_methods(["GET", "POST"])
def list_items(request):
    items = Item.objects.all()

    rendered_page = render(request, "items/items.html", {"items": items, 'form': ItemForm()})
    return HttpResponse(rendered_page)

@require_http_methods(["GET", "POST"])
def update_item(request, id):
    item = Item.objects.get(id=id)

    rendered_page = render(request, "items/update.html", {"item": item, 'form': ItemForm()})
    return HttpResponse(rendered_page)

@require_http_methods(["GET", "POST"])
def update(request, id):
    nome = request.POST.get('nome')
    categoria = request.POST.get('categoria')
    marca = request.POST.get('marca')
    peso = request.POST.get('peso')
    data_validade = request.POST.get('data_validade')

    item = Item.objects.get(id=id)
    item.nome = nome
    item.categoria = categoria
    item.marca = marca
    item.peso = peso
    item.data_validade = data_validade
    item.save()

    return redirect('items:items')

@require_http_methods(["GET", "POST"])
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('items:items')

@require_http_methods(["GET", "POST"])
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
