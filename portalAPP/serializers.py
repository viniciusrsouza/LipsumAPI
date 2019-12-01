from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'
    
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    
    projetos = serializers.SerializerMethodField()

    def get_projetos(self, instance):
        proj_list = []
        a = instance.projeto_set.all()
        for i in a:
            proj_list.append(i.id)
        return proj_list
    
    #projetos = serializers.PrimaryKeyRelatedField(many=True, queryset=Projeto.objects.all())

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UsuarioSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UsuarioSerializer, self).update(instance, validated_data)

    class Meta:
        model = Usuario
        fields = ['id', 'email', 'password', 'nome', 'afiliacao', 'departamento', 'formacao', 'link_lates','photo','projetos','is_superuser']
        extra_kwargs = {'password': {'write_only': True}, 'email': {'write_only': True}, 'is_superuser':{'read_only': True},} 
    
    
'''
class UserUpdateAdminSerializer(serializers.ModelSerializer):
    #all_fields = Usuario._meta.get_fields()
    #print(all_fields)
    #user = Usuario()
    #print(dir(user))
    
    
    class Meta:
        model = Usuario
        fields =  fields = ['id', 'email', 'password', 'nome', 'afiliacao', 'departamento', 'formacao', 'link_lates', 'projetos','photo','is_superuser']
        extra_kwargs = {'password': {'write_only': True}, 'email': {'write_only': True}}
'''