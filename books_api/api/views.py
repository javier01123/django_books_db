from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .models import Author
# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class  = serializers.AuthorSerializer     

