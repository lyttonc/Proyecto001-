from django.urls import path
from AppCoder.views import *

# Con el name le doy un nombre a mi ruta-url, que después voy a incluir en la base
urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('buscar_curso', busqueda_curso, name="AppCoderBuscarCurso"),
    path('guardado', crear_curso, name="AppCoderCurso"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderProfesores"),
    path('todos_cursos', ver_todos_cursos, name="AppCoderTodosCursos"),
]