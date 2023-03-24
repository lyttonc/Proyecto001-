from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import  Curso
# Create your views here.

def cursos(request):
    return render(request, "index.html")

def estudiantes(request):
    pass
def profesores(request):
    pass