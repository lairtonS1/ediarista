from django.shortcuts import render, redirect
from .forms import diarista_form
from .models import Diarista


def cadastrar_diarista(request):
    if request.method == 'POST':
        form_diarista = diarista_form.DiaristaForm(request.POST, request.FILES)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diarista')
    else:
        form_diarista = diarista_form.DiaristaForm()
    return render(request, "form_diarista.html", {'form_diarista': form_diarista})


def listar_diarista(request):
    diaristas = Diarista.objetos.all() 
    return render(request, 'lista_diarista.html', {'diaristas': diaristas})


def editar_diarista(request, diarista_id):
    diarista = Diarista.objetos.get(id=diarista_id)
    if request.method == 'POST':
        form_diarista = diarista_form.DiaristaForm(request.POST or None, request.FILES, instance=diarista)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diarista')
    else:
        form_diarista = diarista_form.DiaristaForm(instance=diarista)
    
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})


def remover_diarista(request, diarista_id):
    diarista = Diarista.objetos.get(id=diarista_id)
    diarista.delete()
    return redirect('listar_diarista')
