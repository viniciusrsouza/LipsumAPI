#from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from .generateToken import get_token


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ProjetoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


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
