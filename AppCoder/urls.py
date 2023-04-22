from django.urls import path
from AppCoder.views import *

# Con el name le doy un nombre a mi ruta-url, que después voy a incluir en la base
urlpatterns = [
    path('myspace', blog, name="AppCoderMySpace"),
    path('buscar_blog', busqueda_blog, name="AppCoderBuscarBlog"),
    path('mis_blogs', busqueda_mis_blog, name="AppCoderBuscarMisBlogs"),
    path('guardado', crear_blog, name="AppCoderGuardarBlog"),
    path('blogs/editar_curso/<titulo>', editar_blog, name="AppCoderEditarBlog"),
    path('blogs/eliminar/<titulo>', eliminar_blog, name="AppCoderEliminarBlog"),
    path('blogs/ver_mas/<titulo>', ver_mas, name="AppCoderVerMas"),
    path('about', about, name="AppCoderAbout"),
    path('blogs', ver_todos_blogs, name="AppCoderBlogs"),
    path('todos_cursos', ver_todos_blogs, name="AppCoderTodosBlogs"),
    path('comentario/<titulo>', crear_comentario, name="AppCoderCrearComentario"),
]