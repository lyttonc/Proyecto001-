from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class miblog(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=100, unique=True)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField(null=True, blank=True)
    imagenblog = models.ImageField(upload_to="image_blog", null=True, blank=True)


    def __str__(self):
        return f"Titulo: {self.titulo}, Subtitulo: {self.subtitulo}"


class micomentario(models.Model):
    usuario_coment = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_coment = models.DateTimeField(auto_now=True)
    comentario= models.TextField(null=True, blank=True)
    blog_coment=models.TextField()


    def __str__(self):
        return f"Comentario: {self.comentario}"

