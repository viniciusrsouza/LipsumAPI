from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        #fields = ['id', 'email', 'password', 'nome', 'afiliacao', 'departamento', 'formacao', 'link_lates']

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class ProjetoParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetoParticipantes
        fields = '__all__'