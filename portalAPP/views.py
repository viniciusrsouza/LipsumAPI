from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
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
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioView(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer2(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        

class ProjetoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class ProjetoParticipantesViewSet(viewsets.ModelViewSet):
    queryset = ProjetoParticipantes.objects.all()
    serializer_class = ProjetoParticipantesSerializer


class GerarLink(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        token_auth = TokenAuth(token=get_token())
        while True:
            try:
                token_auth.save()
                break
            except:
                pass
        content = {'Token': token_auth.token}
        return Response(content)

class AutenticarLink(APIView):
    def get(self,request, id):
        try:
            token = get_object_or_404(TokenAuth, pk=id)
            token.delete()
            content = {'Autenticado': True}
            return Response(content)
        except:
            content = {'Autenticado': False}
            return Response(content)
