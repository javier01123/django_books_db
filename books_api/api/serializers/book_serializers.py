from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import Book, Author
from . import author_serializers 


class BookSerializer(ModelSerializer):    
    authors = serializers.PrimaryKeyRelatedField(many = True, queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = '__all__'       
    def validate(self, data):                                  
        if not any(data.get('authors')):            
            raise serializers.ValidationError({'authors':'This field may not be empty.'}) 
        return data

class BookPatchSerializer(ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many = True, queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = '__all__' 
    def validate(self, data):       
        authors = data.get('authors')        
        if authors is None:
            return data
        if not any(authors):            
            raise serializers.ValidationError({'authors':'This field may not be empty.'}) 
        return data

class BookRetriveSerializer(ModelSerializer):
    authors = author_serializers.AuthorSerializer(many = True)
    class Meta:
        model = Book
        fields = '__all__'

class BookListSerializer(ModelSerializer):    
    class Meta:
        model = Book         
        exclude = ('authors',)
