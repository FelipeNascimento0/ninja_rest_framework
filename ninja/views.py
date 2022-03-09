from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import UserSerializer, Groupserializer

class UserViewSet(viewsets.ModelViewSet):
    '''Endpoint da API que permite que os usuários sejam visualizados ou editados'''

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    '''
Endpoint de API que permite que grupos sejam visualizados ou editados'''

    queryset = Group.objects.all()
    serializer_class = Groupserializer
    permission_classes = [permissions.IsAuthenticated]
