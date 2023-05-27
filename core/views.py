from django.shortcuts import render, redirect
from .models import Usuario
def home(request):
    return render(request, "users/index.html")

def save_user(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')

    Usuario.objects.create(nome=nome,
                        email=email,
                        cpf=cpf,
                        telefone=telefone)
    return render(request, 'users/index.html')


def list_users(request):
    usuarios = Usuario.objects.all()

    return render(request, "users/users.html", {"usuarios": usuarios})

def update_user(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "users/update.html", {"usuario": usuario})

def update(request, id):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')

    usuario = Usuario.objects.get(id=id)

    usuario.nome = nome
    usuario.email = email
    usuario.cpf = cpf
    usuario.telefone = telefone
    usuario.save()

    return redirect('users:users')

def delete_user(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('users:users')

def search_users(request):
    s_nome = request.POST.get('search')
    if s_nome:
        usuarios = Usuario.objects.filter(nome__icontains=s_nome)
        return render(request, "users/search.html", {"usuarios": usuarios})
    else:
        usuarios =""
        return render(request, "users/search.html", {"usuarios": usuarios})
