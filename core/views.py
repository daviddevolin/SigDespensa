from django.shortcuts import render, redirect
from .models import Usuario
def home(request):
    return render(request, "index.html")

def saveUser(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')

    Usuario.objects.create(nome=nome,
                        email=email,
                        cpf=cpf,
                        telefone=telefone)
    return render(request, 'index.html')


def listUsers(request):
    usuarios = Usuario.objects.all()

    return render(request, "users.html", {"usuarios": usuarios})

def updateUser(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "update.html", {"usuario": usuario})

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

    return redirect(listUsers)

def deleteUser(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(listUsers)