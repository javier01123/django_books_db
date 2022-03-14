from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers
from .models import Author,Book


# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class  = serializers.AuthorSerializer     

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

