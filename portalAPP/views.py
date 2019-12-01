from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from .generateToken import get_token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .email import send_link
from .customPermissions import *


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'nome': user.nome,
            'Administrador': user.is_superuser
            
        })


class UsuarioViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioView(APIView):
    #Lista todos os usuários, ou cria um novo
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)


class UsuarioRegister(APIView):
    
    def post(self, request, token):
        serializer = UsuarioSerializer(data=request.data)
        try:
            token = get_object_or_404(TokenAuth, pk=token)
            if serializer.is_valid():
                serializer.save()
                token.delete()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        
    
class UsuarioDetalhe(APIView):
    permission_classes = [IsOwnerAccountOrAdminOrReadOnly]

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
#Método de views baseadas em funções
@api_view(['GET', 'PUT', 'DELETE'])
def usuarioDetalhe(request, id):

    try:
        usuario = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer2(usuario)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''        


class ProjetoView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    #Lista todos os projetos, ou cria um novo
    def get(self, request):
        projetos = Projeto.objects.all()
        serializer = ProjetoSerializer(projetos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjetoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjetoDetalhe(APIView):
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_object(self, pk):
        try:
            obj = Projeto.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Projeto.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        projeto = self.get_object(pk)
        serializer = ProjetoSerializer(projeto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        projeto = self.get_object(pk)
        serializer = ProjetoSerializer(projeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        projeto = self.get_object(pk)
        projeto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoticiaView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    #Lista todas as noticias, ou cria uma nova
    def get(self, request):
        noticias = Noticia.objects.all()
        serializer = NoticiaSerializer(noticias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoticiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticiaDetalhe(APIView):
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_object(self, pk):
        try:
            obj = Noticia.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Noticia.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        noticia = self.get_object(pk)
        serializer = NoticiaSerializer(noticia)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        noticia = self.get_object(pk)
        serializer = NoticiaSerializer(noticia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        noticia = self.get_object(pk)
        noticia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventoView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    #Lista todos os projetos, ou cria um novo
    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventoDetalhe(APIView):
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_object(self, pk):
        try:
            obj = Evento.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Evento.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        evento = self.get_object(pk)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        evento = self.get_object(pk)
        serializer = EventoSerializer(evento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        evento = self.get_object(pk)
        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GerarLink(APIView):
    #permission_classes = (IsAdminUser,)

    def get(self,request,email):
        token = get_token()
        send_link(email, token)
        content = {'Token': token}
        return Response(content)

class AutenticarLink(APIView):
    def get(self,request, id):
        try:
            token = get_object_or_404(TokenAuth, pk=id)
            content = {'Autenticado': True}
            return Response(content)
        except:
            content = {'Autenticado': False}
            return Response(content)
