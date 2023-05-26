from django.shortcuts import render, redirect
from .models import Item

def home(request):
    return render(request, "index.html")

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
    
    return render(request, 'index.html')

def list_items(request):
    items = Item.objects.all()
    return render(request, "items.html", {"items": items})

def update_item(request, id):
    item = Item.objects.get(id=id)
    return render(request, "update.html", {"item": item})

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

    return redirect(list_items)

def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect(list_items)

def search_items(request):
    s_nome = request.POST.get('search')
    if s_nome:
        items = Item.objects.filter(nome__icontains=s_nome)
        return render(request, "search.html", {"items": items})
    else:
        items = ""
        return render(request, "search.html", {"items": items})
