from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'password', 'nome', 'afiliacao', 'departamento', 'formacao', 'link_lates']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UsuarioSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UsuarioSerializer, self).update(instance, validated_data)
    

class UsuarioSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        #extra_kwargs = {'password': {'write_only': True}}   


class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class ProjetoParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetoParticipantes
        fields = '__all__'