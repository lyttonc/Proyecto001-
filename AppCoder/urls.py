from django.urls import path
from AppCoder.views import *

# Con el name le doy un nombre a mi ruta-url, que después voy a incluir en la base
urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('curso/<nombre>/<camada>', crear_curso, name="AppCoderCurso"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderProfesores"),
]