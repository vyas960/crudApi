from django.shortcuts import render
from rest_framework import viewsets
from testApp import serializers
from django.contrib.auth.models import User
# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
