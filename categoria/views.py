from django.shortcuts import render, redirect
from .models import Categoria
from .forms import CategoriaForm
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, "categories/index.html", {'form': CategoriaForm()})

@require_http_methods(["GET", "POST"])
def save_category(request):
    nome = request.POST.get('nome')
    Categoria.objects.create(nome=nome)
    return render(request, 'categories/index.html', {'form': CategoriaForm()})

@require_http_methods(["GET", "POST"])
def list_categories(request):
    categorias = Categoria.objects.all()
    return render(request, "categories/categories.html", {"categorias": categorias})

@require_http_methods(["GET", "POST"])
def update_category(request, id):
    categoria = Categoria.objects.get(id=id)
    return render(request, "categories/update.html", {"categoria": categoria, 'form':CategoriaForm()})

@require_http_methods(["GET", "POST"])
def update(request, id):
    nome = request.POST.get('nome')
    categoria = Categoria.objects.get(id=id)

    categoria.nome = nome
    categoria.save()

    return redirect('categories:categories')

@require_http_methods(["GET", "POST"])
def delete_category(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categories:categories')

@require_http_methods(["GET", "POST"])
def search_categories(request):
    s_nome = request.POST.get('search')
    if s_nome:
        categorias = Categoria.objects.filter(nome__icontains=s_nome)
        return render(request, "categories/search.html", {"categorias": categorias})
    else:
        categorias =""
        return render(request, "categories/search.html", {"categorias": categorias})
