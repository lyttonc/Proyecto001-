from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import  Curso
# Create your views here.

def guardar_curso(reques,camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()
    return HttpResponse("Usuario creado exitos  amente")