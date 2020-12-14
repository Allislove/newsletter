from django.shortcuts import render
from django.shortcuts import get_object_or_404
from usuarios.serializers import UserSerializer
from usuarios.models import Usuario
from rest_framework import viewsets
from rest_framework.response import Response



# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

