from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def interessado(request):
    return render(request, 'accounts/interessado.html')

def terra(request):
    return render(request, 'accounts/terras.html')