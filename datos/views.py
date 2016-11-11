from django.shortcuts import render
from django.http import HttpResponse


def hola(request):
    return render(request, "index.html", {"nombre": "Reyes :3"})


def formulario(request):
    form ="hola a mi formulario"
    return render(request, "formulario.html", {"formulario": form})

# Create your views here.
