from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    listaProcessos = Processo.objects.all()
    listaInteressados = Interessado.objects.all()
    listaSetor = Setor.objects.all()

    totalProcessos = listaProcessos.count()
    prontos = listaProcessos.filter(status='Finalizado').count()
    pendente = listaProcessos.filter(status='Pendente').count()
    cancelado = listaProcessos.filter(status='Cancelado').count()

    context = {'listaP':listaProcessos, 'listaI':listaInteressados, 'listaS':listaSetor
    , 'totalProcessos':totalProcessos, 'prontos':prontos, 'pendente':pendente, 'cancelado':cancelado}
    return render(request, 'accounts/dashboard.html', context)

def interessadopg(request):
    return render(request, 'accounts/interessado.html')

def terrapg(request):
    lista = Terra.objects.all()
    return render(request, 'accounts/terras.html', {'lista':lista})