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
    diaristas = Diarista.objects.all() #equivale a select *from Diaristas
    return render(request, 'lista_diarista.html', {'diaristas':diaristas})
