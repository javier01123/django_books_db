from rest_framework.serializers import ModelSerializer
from . import models

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = models.Author
        fields = ['id','first_name','last_name']