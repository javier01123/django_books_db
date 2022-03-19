from api.models import Author
from rest_framework.serializers import ModelSerializer

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','first_name','last_name']