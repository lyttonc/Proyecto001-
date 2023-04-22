from django import forms

class BlogForm(forms.Form):
    titulo = forms.CharField(min_length=10, max_length=100)
    subtitulo = forms.CharField(min_length=10, max_length=100)
    cuerpo = forms.CharField()
    imagenblog = forms.ImageField()


class BusquedaBlogForm(forms.Form):
    titulo = forms.CharField(min_length=3, max_length=40)


class ComentarioForm(forms.Form):
    comentario = forms.CharField(min_length=10, max_length=10000)
