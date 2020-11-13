from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    listaProcessos = Processo.objects.all()
    listaInteressados = Interessado.objects.all()
    listaTerras = Terra.objects.all()

    totalProcessos = listaProcessos.count()
    prontos = listaProcessos.filter(status='Finalizado').count()
    pendente = listaProcessos.filter(status='Pendente').count()
    cancelado = listaProcessos.filter(status='Cancelado').count()

    context = {'listaP':listaProcessos, 'listaI':listaInteressados, 'listaT':listaTerras
    , 'totalProcessos':totalProcessos, 'prontos':prontos, 'pendente':pendente, 'cancelado':cancelado}
    return render(request, 'accounts/dashboard.html', context)

def criarInteressado(request):

    form = InteressadoForm()
    if request.method == 'POST':
        form = InteressadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

def interessadopg(request, pk):
    interessado = Interessado.objects.get(id=pk)
    processos = interessado.processo_set.all()
    processosCount = processos.count()

    context = {'interessado': interessado, 'processos': processos,'processosCount': processosCount}
    return render(request, 'accounts/interessado.html', context)

def terrapg(request):
    lista = Terra.objects.all()
    return render(request, 'accounts/terras.html', {'lista':lista})

def criarProcesso(request):

    form = ProcessoForm()
    if request.method == 'POST':
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

def verProcesso(request, pk):
    processo = Processo.objects.get(id=pk)
    form = ProcessoForm(instance=processo)

    if request.method == 'POST':
        form = ProcessoForm(request.POST, instance=processo)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

def criarTerra(request):

    form = TerraForm()
    if request.method == 'POST':
        form = TerraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

def verTerra(request, pk):
    processo = Terra.objects.get(id=pk)
    form = TerraForm(instance=processo)

    if request.method == 'POST':
        form = TerraForm(request.POST, instance=processo)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

def deleteProcesso(request, pk):
    processo = Processo.objects.get(id=pk)
    if request.method == 'POST':
        processo.delete()
        return redirect('/')

    context = {'item':processo}

    return render(request, 'accounts/delete.html', context)

def deleteTerra(request, pk):
    processo = Terra.objects.get(id=pk)
    if request.method == 'POST':
        processo.delete()
        return redirect('/')

    context = {'item':processo}

    return render(request, 'accounts/delete.html', context)