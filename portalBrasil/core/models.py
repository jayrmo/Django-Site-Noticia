from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, blank=True)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    fonte = models.CharField(max_length=255, blank=True)
    local = models.CharField(max_length=100, blank=True)
    imagem_url = models.ImageField(null=True,blank=True)
    categoria = models.ForeignKey(Categoria, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo
    
    
