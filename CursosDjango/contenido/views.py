from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'vistas/inicio.html')

def contacto(request):
    return render(request, 'vistas/contacto.html')

def cursos(request):
    return render(request, 'vistas/cursos.html')