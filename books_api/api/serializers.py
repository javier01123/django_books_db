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
    
    def __init__(self, *args, **kwargs):        
        if kwargs['context']['view'].action == 'list':
            del self.fields['authors']
        super().__init__(*args, **kwargs)

    def validate(self, data):     
        method = self.context.get('request').method          
        has_authors_key = 'authors' in data
        contains_authors = has_authors_key and len(data['authors']) > 0

        """only allow null authors on PATCH"""        
        if method == 'PATCH' and not has_authors_key:
            return data

        if not contains_authors:            
            raise serializers.ValidationError({'authors':'This field may not be empty.'}) 

        return data
