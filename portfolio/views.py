import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def DiaDeHoy(request):
    dia = datetime.datetime.now()
    documentodeTexto = f'Hoy es dia: <br> {dia}'
    return HttpResponse(documentodeTexto)

