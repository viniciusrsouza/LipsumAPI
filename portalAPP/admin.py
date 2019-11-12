from django.contrib import admin
from .models import Usuario
from .models import *

admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(ProjetoParticipantes)
admin.site.register(TokenAuth)
admin.site.register(Noticia)