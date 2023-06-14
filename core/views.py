from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def home(request):
    usuario_form = UsuarioForm()

    rendered_page = render(request, "users/index.html", {"form": usuario_form})

    return HttpResponse(rendered_page)

@require_http_methods(["GET", "POST"])
def save_user(request):

    form = UsuarioForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data

        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        cpf = cleaned_data.get('cpf')
        telefone = cleaned_data.get('telefone')

        Usuario.objects.create(nome=nome,
                            email=email,
                            cpf=cpf,
                            telefone=telefone) 
        
        rendered_page = render(request, 'users/index.html', {"form": UsuarioForm()})
        return HttpResponse(rendered_page)
    else:
        rendered_page = render(request, 'users/index.html', {"form": UsuarioForm(), "errors": form.errors})
        return HttpResponse(rendered_page)


@require_http_methods(["GET", "POST"])
def list_users(request):
    usuarios = Usuario.objects.all()

    rendered_page = render(request, "users/users.html", {"usuarios": usuarios})
    return HttpResponse(rendered_page)

@require_http_methods(["GET", "POST"])
def update_user(request, id):
    usuario = Usuario.objects.get(id=id)

    rendered_page = render(request, "users/update.html", {"usuario": usuario, "form": UsuarioForm()})
    return HttpResponse(rendered_page)

@require_http_methods(["GET", "POST"])
def update(request, id):
    form = UsuarioForm(request.POST)
    usuario = Usuario.objects.get(id=id)
    
    if form.is_valid():
        cleaned_data = form.cleaned_data
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        cpf = cleaned_data.get('cpf')
        telefone = cleaned_data.get('telefone')


        usuario.nome = nome
        usuario.email = email
        usuario.cpf = cpf
        usuario.telefone = telefone
        usuario.save()

        return redirect('users:users')
    else:

        rendered_page = render(request, 'users/update.html', {"usuario": usuario,"form": UsuarioForm(), "errors": form.errors})
        return HttpResponse(rendered_page)

@require_http_methods(["GET", "POST"])
def delete_user(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('users:users')

@require_http_methods(["GET", "POST"])
def search_users(request):
    s_nome = request.POST.get('search')
    if s_nome:
        usuarios = Usuario.objects.filter(nome__icontains=s_nome)

        rendered_page = render(request, "users/search.html", {"usuarios": usuarios})

        return HttpResponse(rendered_page)
    else:
        usuarios =""

        rendered_page = render(request, "users/search.html", {"usuarios": usuarios})

        return HttpResponse(rendered_page)
