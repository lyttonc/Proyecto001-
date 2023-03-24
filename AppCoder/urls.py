from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('curso',cursos),
    path('estudiantes',estudiantes),
    path('profesores',profesores),
]