from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.permissions import IsAuthenticated
from .managers import CustomUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone

class Usuario (AbstractUser):
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #permission_classes = (IsAuthenticated,)
    objects = CustomUserManager()

    nome = models.CharField(max_length = 200)
    afiliacao = models.CharField(max_length = 200)
    departamento = models.CharField(max_length = 200)
    formacao = models.CharField(max_length = 200)
    link_lates = models.CharField(max_length = 300)
    photo = models.ImageField(upload_to = 'profileImgs', blank=True)

    def __str__(self):
        return self.email


class TokenAuth(models.Model):
    token = models.CharField(max_length = 50, primary_key=True)

class Projeto(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='autor')
    titulo = models.CharField(max_length = 200, unique = True)
    link_projeto = models.CharField(max_length = 300, blank = True)
    categoria = models.CharField(max_length = 200,  default = "")
    descricao = models.TextField(max_length = 2000)
    imagem = models.ImageField(upload_to = 'projImgs')
    data_publicacao = models.DateField(auto_now_add = True)
    participantes = models.ManyToManyField(Usuario)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length = 200, unique = True)
    categoria = models.CharField(max_length=200, blank=True)
    descricao = models.TextField(max_length = 2000)
    imagem = models.ImageField(upload_to = 'noticiaImgs')
    data_publicacao = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.titulo

class Evento(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='autor_evento')
    titulo = models.CharField(max_length = 200, unique = True)
    descricao = models.TextField(max_length = 2000)
    #imagem = models.ImageField(upload_to = 'noticiaImgs')
    #participantes = models.ManyToManyField(Usuario)
    data_publicacao = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.titulo
    
    def validate_date(data):
        if data < timezone.now():
            raise ValidationError("Date cannot be in the past")
    
    data = models.DateTimeField(validators=[validate_date])