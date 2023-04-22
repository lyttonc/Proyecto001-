from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from AppCoder.models import miblog, micomentario
from AppCoder.forms import BlogForm, BusquedaBlogForm, ComentarioForm


# Create your views here.
@login_required
def blog(request):

    all_blogs = miblog.objects.all()
    context = {
        "blogs": all_blogs,
        "form": BlogForm(),
        "form_busqueda": BusquedaBlogForm(),
    }
    return render(request, "AppCoder/myspace.html", context=context)

@login_required
def crear_blog(request):
    if request.method == "POST":
        mi_formulario = BlogForm(request.POST, request.FILES)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            blog_save = miblog(
                titulo=informacion['titulo'],
                subtitulo=informacion['subtitulo'],
                cuerpo=informacion['cuerpo'],
                imagenblog=informacion['imagenblog'],
                usuario=request.user
            )
            blog_save.save()

    return render(request, "AppCoder/save_blog.html")

@login_required
def busqueda_blog(request):
    #mostrar datos filtrado
    mi_formulario=BusquedaBlogForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        blogs_filtrado = miblog.objects.filter(titulo__icontains=informacion['titulo'])
        context = {
            "blogs": blogs_filtrado
        }
    return render(request, "AppCoder/busqueda_blog.html", context=context)

@login_required
def busqueda_mis_blog(request):

    all_blogs = miblog.objects.filter(usuario=request.user)
    context = {
        "blogs": all_blogs,
        "form_busqueda": BusquedaBlogForm()
    }

    return render(request, "AppCoder/ver_mis_blogs.html", context=context)
def ver_todos_blogs(request):
    #mostrar datos no filtrado
    all_blogs = miblog.objects.all()
    context = {
        "blogs": all_blogs,
        "form_busqueda": BusquedaBlogForm()
    }
    return render(request, "AppCoder/ver_todos_blogs.html", context=context)

@login_required
def eliminar_blog(request, titulo):
    get_blog = miblog.objects.get(titulo=titulo)
    get_blog.delete()

    return redirect("AppCoderMySpace")

@login_required
def editar_blog(request, titulo):
    get_blog = miblog.objects.get(titulo=titulo)
    if request.method == "POST":
        mi_formulario = BlogForm(request.POST, request.FILES)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_blog.titulo=informacion['titulo']
            get_blog.subtitulo=informacion['subtitulo']
            get_blog.cuerpo=informacion['cuerpo']
            get_blog.imagenblog=informacion['imagenblog']

            get_blog.save()
            return redirect("AppCoderMySpace")

    context={
        "titulo": titulo,
        "form": BlogForm(initial={
            "titulo": get_blog.titulo,
            "subtitulo": get_blog.subtitulo,
            "cuerpo": get_blog.cuerpo,
            "imagenblog":get_blog.imagenblog
        })
    }
    return render(request, "AppCoder/editar_blog.html", context=context)

def about(request):
    return render(request, "AppCoder/about.html")

def ver_mas(request, titulo):
    #mostrar datos filtrado
    get_blog = miblog.objects.get(titulo=titulo)
    all_comentario = micomentario.objects.filter(blog_coment=titulo)
    context = {
        "blogs": get_blog,
        "form": ComentarioForm(),
        "comentario": all_comentario
    }
    return render(request, "AppCoder/vermas.html", context=context)

@login_required()
def crear_comentario(request, titulo):
    get_blog = miblog.objects.get(titulo=titulo)
    if request.method == "POST":
        mi_formulario = ComentarioForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            comentario_save = micomentario(
                usuario_coment=request.user,
                comentario=informacion['comentario'],
                blog_coment=get_blog.titulo
            )
            comentario_save.save()

    return render(request, "AppCoder/gracias_comentario.html")

