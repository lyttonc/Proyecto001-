from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoForm, BusquedaCursoForm


# Create your views here.
@login_required
def cursos(request):

    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form": CursoForm(),
        "form_busqueda": BusquedaCursoForm(),
    }
    return render(request, "AppCoder/cursos.html", context=context)

@login_required
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

@login_required
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

@login_required
def ver_todos_cursos(request):
    #mostrar datos no filtrado
    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos
    }
    return render(request, "AppCoder/ver_todos_cursos.html", context=context)

@login_required
def eliminar_curso(request, camada):
    get_curso = Curso.objects.get(camada=camada)
    get_curso.delete()

    return redirect("AppCoderCursos")

@login_required
def editar_curso(request, camada):
    get_curso = Curso.objects.get(camada=camada)
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_curso.nombre=informacion['nombre']
            get_curso.camada=informacion['camada']

            get_curso.save()
            return redirect("AppCoderCursos")

    context={
        "camada": camada,
        "form": CursoForm(initial={
            "nombre": get_curso.nombre,
            "camada": get_curso.camada
        })
    }
    return render(request, "AppCoder/editar_curso.html", context=context)

@login_required
def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

@login_required
def profesores(request):
    return render(request, "AppCoder/profesores.html")

@login_required
def todos_cursos(request):
    return render(request, "AppCoder/ver_todos_cursos.html")

