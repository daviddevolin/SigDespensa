from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm

from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_safe, require_POST
from django.contrib.auth.decorators import login_required

from allauth.account.forms import LoginForm

@require_safe
def home(request):
    usuario_form = UsuarioForm()

    rendered_page = render(request, "users/index.html", {"usuario_form": usuario_form})

    return HttpResponse(rendered_page)

@require_POST
def save_user(request):

    usuario_form = UsuarioForm(request.POST)

    if usuario_form.is_valid():
        cleaned_data_usuario = usuario_form.cleaned_data


        username = cleaned_data_usuario.get('username')
        primeiro_nome = cleaned_data_usuario.get('first_name')
        sobrenome = cleaned_data_usuario.get('last_name')
        email = cleaned_data_usuario.get('email')
        senha = cleaned_data_usuario.get('password')
        cpf = cleaned_data_usuario.get('cpf')
        telefone = cleaned_data_usuario.get('telefone')

        Usuario.objects.create_user(username=username,
                                email=email,
                                first_name=primeiro_nome,
                                last_name=sobrenome,
                                password=senha,
                                cpf=cpf,
                                telefone=telefone)


        
        rendered_page = render(request, 'users/index.html', {"usuario_form": UsuarioForm()})
        return HttpResponse(rendered_page)
    else:
        rendered_page = render(request, 'users/index.html', {"usuario_form": UsuarioForm(), "errors": usuario_form.errors})
        return HttpResponse(rendered_page)


@require_safe
def list_users(request):
    usuarios = Usuario.objects.all()

    rendered_page = render(request, "users/users.html", {"usuarios": usuarios})
    return HttpResponse(rendered_page)

@require_safe
def update_user(request, id):
    usuario = Usuario.objects.get(id=id)

    rendered_page = render(request, "users/update.html", {"usuario": usuario, "usuario_form": UsuarioForm()})
    return HttpResponse(rendered_page)

@require_POST
def update(request, id):
    usuario_form = UsuarioForm(request.POST)
    

    usuario = Usuario.objects.get(id=id)
    
    if usuario_form.is_valid():
        usuario_cleaned_data = usuario_form.cleaned_data
        nome = usuario_cleaned_data.get('first_name')
        sobrenome = usuario_cleaned_data.get('last_name')
        email = usuario_cleaned_data.get('email')
        cpf = usuario_cleaned_data.get('cpf')
        telefone = usuario_cleaned_data.get('telefone')


        usuario.first_name = nome
        usuario.last_name = sobrenome
        usuario.email = email
        usuario.cpf = cpf
        usuario.telefone = telefone
        usuario.save()

        return redirect('users:users')
    else:

        rendered_page = render(request, 'users/update.html', {"usuario": usuario, "usuario_form": UsuarioForm() ,"errors": usuario_form.errors})
        return HttpResponse(rendered_page)

@require_safe
def delete_user(request, id):
    usuario = Usuario.objects.get(id=id)

    usuario.delete()
    return redirect('users:users')

@require_POST
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

@require_safe
def login (request):
    rendered_page= render(request, "users/login.html", {"login_form": LoginForm()})
    return rendered_page

@login_required
@require_safe
def auth_login (request):
    m = Usuario.objects.get(username=request.user.username)
    print(m.first_name)
    rendered_page = render(request, "users/test.html")
    return rendered_page