from django.shortcuts import render
from django.shortcuts import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoForm, BusquedaCursoForm


# Create your views here.
def cursos(request):

    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form": CursoForm(),
        "form_busqueda": BusquedaCursoForm(),
    }
    return render(request, "AppCoder/cursos.html", context=context)


def crear_curso(request):
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=informacion['nombre'],
                camada=informacion['camada']
            )
            curso_save.save()

    return render(request, "AppCoder/save_curso.html")


def busqueda_curso(request):
    #mostrar datos filtrado
    mi_formulario=BusquedaCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrado = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrado
        }
    return render(request, "AppCoder/busqueda_curso.html", context=context)

def ver_todos_cursos(request):
    #mostrar datos no filtrado
    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos
    }
    return render(request, "AppCoder/ver_todos_cursos.html", context=context)


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def profesores(request):
    return render(request, "AppCoder/profesores.html")

def todos_cursos(request):
    return render(request, "AppCoder/ver_todos_cursos.html")

