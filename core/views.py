from django.shortcuts import render
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