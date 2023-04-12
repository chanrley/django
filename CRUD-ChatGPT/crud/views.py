from django.shortcuts import render, redirect
from .models import Exemplo
from .forms import ExemploForm

def lista_exemplos(request):
    exemplos = Exemplo.objects.all()
    return render(request, 'lista_exemplos.html', {'exemplos': exemplos})

def novo_exemplo(request):
    form = ExemploForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_exemplos')
    return render(request, 'exemplo_form.html', {'form': form})

def edita_exemplo(request, id):
    exemplo = Exemplo.objects.get(id=id)
    form = ExemploForm(request.POST or None, instance=exemplo)
    if form.is_valid():
        form.save()
        return redirect('lista_exemplos')
    return render(request, 'exemplo_form.html', {'form': form})

def remove_exemplo(request, id):
    exemplo = Exemplo.objects.get(id=id)
    exemplo.delete()
    return redirect('lista_exemplos')
