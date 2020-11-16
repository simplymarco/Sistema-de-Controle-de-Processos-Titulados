from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import ProcessoFilter, TerraFilter, InteressadoFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Usuario ou senha incorretos')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
def criarInteressado(request):

    form = InteressadoForm()
    if request.method == 'POST':
        form = InteressadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

@login_required(login_url='login')
def editarInteressado(request, pk):
    interessado = Interessado.objects.get(id=pk)
    form = InteressadoForm(instance=interessado)

    if request.method == 'POST':
        form = InteressadoForm(request.POST, instance=interessado)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

@login_required(login_url='login')
def deleteInteressado(request, pk):
    interessado = Interessado.objects.get(id=pk)
    if request.method == 'POST':
        interessado.delete()
        return redirect('/')

    context = {'item':interessado}

    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def interessadopg(request, pk):
    interessado = Interessado.objects.get(id=pk)
    processos = interessado.processo_set.all()
    processosCount = processos.count()

    myFilter = ProcessoFilter(request.GET, queryset=processos)
    processos = myFilter.qs

    context = {'interessado': interessado, 'processos': processos,'processosCount': processosCount, 'myFilter':myFilter}
    return render(request, 'accounts/interessado.html', context)

@login_required(login_url='login')
def interessadolist(request):
    lista = Interessado.objects.all()

    myFilter = InteressadoFilter(request.GET, queryset=lista)
    lista = myFilter.qs

    return render(request, 'accounts/interessadolist.html', {'lista':lista,'myFilter':myFilter})

@login_required(login_url='login')
def criarProcesso(request):

    form = ProcessoForm()
    if request.method == 'POST':
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteProcesso(request, pk):
    processo = Processo.objects.get(id=pk)
    if request.method == 'POST':
        processo.delete()
        return redirect('/')

    context = {'item':processo}

    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def processolist(request):
    lista = Processo.objects.all()

    myFilter = ProcessoFilter(request.GET, queryset=lista)
    lista = myFilter.qs

    return render(request, 'accounts/processolist.html', {'lista':lista, 'myFilter':myFilter})

@login_required(login_url='login')
def criarTerra(request):

    form = TerraForm()
    if request.method == 'POST':
        form = TerraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteTerra(request, pk):
    processo = Terra.objects.get(id=pk)
    if request.method == 'POST':
        processo.delete()
        return redirect('/')

    context = {'item':processo}

    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def terralist(request):
    lista = Terra.objects.all()

    myFilter = TerraFilter(request.GET, queryset=lista)
    lista = myFilter.qs

    return render(request, 'accounts/terras.html', {'lista':lista, 'myFilter':myFilter})

@login_required(login_url='login')
def criarSetor(request):

    form = SetorForm()
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

@login_required(login_url='login')
def verSetor(request, pk):
    processo = Setor.objects.get(id=pk)
    form = SetorForm(instance=processo)

    if request.method == 'POST':
        form = SetorForm(request.POST, instance=processo)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'accounts/ver_form.html', context)

@login_required(login_url='login')
def deleteSetor(request, pk):
    processo = Setor.objects.get(id=pk)
    if request.method == 'POST':
        processo.delete()
        return redirect('/')

    context = {'item':processo}

    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def setorlist(request):
    lista = Setor.objects.all()
    return render(request, 'accounts/setorlist.html', {'lista':lista})

