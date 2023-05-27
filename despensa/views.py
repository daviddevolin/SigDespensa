from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Despensa

def despensa_list(request):
    despensas = Despensa.objects.all()
    return render(request, 'despensa/list.html', {'despensas': despensas})

def despensa_detail(request, pk):
    despensa = get_object_or_404(Despensa, pk=pk)
    return render(request, 'despensa/detail.html', {'despensa': despensa})

def despensa_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantTotal = request.POST.get('quantTotal')
        capacidade = request.POST.get('capacidade')
        categoria = request.POST.get('categoria')
        Despensa.objects.create(nome=nome, quantTotal=quantTotal, capacidade=capacidade, categoria=categoria)
        return redirect('despensa_list')
    return render(request, 'despensa/form.html')

def despensa_update(request, pk):
    despensa = get_object_or_404(Despensa, pk=pk)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantTotal = request.POST.get('quantTotal')
        capacidade = request.POST.get('capacidade')
        categoria = request.POST.get('categoria')
        despensa.nome = nome
        despensa.quantTotal = quantTotal
        despensa.capacidade = capacidade
        despensa.categoria = categoria
        despensa.save()
        return redirect('despensa_list')
    return render(request, 'despensa/form.html', {'despensa': despensa})

def despensa_delete(request, pk):
    despensa = get_object_or_404(Despensa, pk=pk)
    if request.method == 'POST':
        despensa.delete()
        return redirect('despensa_list')
    return render(request, 'despensa/confirm_delete.html', {'despensa': despensa})
