from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home")

def interessado(request):
    return HttpResponse("Interessado")

def processo(request):
    return HttpResponse("Processo")