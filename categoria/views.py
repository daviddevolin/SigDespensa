from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria
from .forms import CategoriaForm
from django.views.decorators.http import require_safe, require_POST
# Create your views here.

@require_safe
def home(request):

    rendered_page =  render(request, "categories/index.html", {'form': CategoriaForm()})
    return HttpResponse(rendered_page)

@require_POST
def save_category(request):
    nome = request.POST.get('nome')
    Categoria.objects.create(nome=nome)

    rendered_page = render(request, 'categories/index.html', {'form': CategoriaForm()})
    return HttpResponse(rendered_page)

@require_safe
def list_categories(request):
    categorias = Categoria.objects.all()


    rendered_page = render(request, "categories/categories.html", {"categorias": categorias})
    return HttpResponse(rendered_page)

@require_safe
def update_category(request, id):
    categoria = Categoria.objects.get(id=id)

    rendered_page = render(request, "categories/update.html", {"categoria": categoria, 'form':CategoriaForm()})
    return HttpResponse(rendered_page)

@require_POST
def update(request, id):
    nome = request.POST.get('nome')
    categoria = Categoria.objects.get(id=id)

    categoria.nome = nome
    categoria.save()

    return redirect('categories:categories')

@require_safe
def delete_category(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categories:categories')

@require_POST
def search_categories(request):
    s_nome = request.POST.get('search')
    if s_nome:
        categorias = Categoria.objects.filter(nome__icontains=s_nome)

        rendered_page = render(request, "categories/search.html", {"categorias": categorias})
        return HttpResponse(rendered_page)
    else:
        categorias =""

        rendered_page = render(request, "categories/search.html", {"categorias": categorias})
        return HttpResponse(rendered_page)
