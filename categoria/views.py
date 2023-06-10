from django.shortcuts import render, redirect
from .models import Categoria
from .forms import CategoriaForm
# Create your views here.
def home(request):
    return render(request, "categories/index.html", {'form': CategoriaForm()})

def save_category(request):
    nome = request.POST.get('nome')
    Categoria.objects.create(nome=nome)
    return render(request, 'categories/index.html', {'form': CategoriaForm()})

def list_categories(request):
    categorias = Categoria.objects.all()
    return render(request, "categories/categories.html", {"categorias": categorias})

def update_category(request, id):
    categoria = Categoria.objects.get(id=id)
    return render(request, "categories/update.html", {"categoria": categoria, 'form':CategoriaForm()})

def update(request, id):
    nome = request.POST.get('nome')
    categoria = Categoria.objects.get(id=id)

    categoria.nome = nome
    categoria.save()

    return redirect('categories:categories')

def delete_category(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categories:categories')

def search_categories(request):
    s_nome = request.POST.get('search')
    if s_nome:
        categorias = Categoria.objects.filter(nome__icontains=s_nome)
        return render(request, "categories/search.html", {"categorias": categorias})
    else:
        categorias =""
        return render(request, "categories/search.html", {"categorias": categorias})
