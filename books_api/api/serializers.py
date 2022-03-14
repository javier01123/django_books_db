from operator import truediv
from pprint import pprint
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Book,Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','first_name','last_name']


class BookSerializer(ModelSerializer):    
    authors = serializers.PrimaryKeyRelatedField(many = True, queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = '__all__'  
    
    def validate(self, data):     
        if len(self.initial_data['authors']) == 0:            
            raise serializers.ValidationError({'authors':'This field may not be blank.'}) 
        return data
