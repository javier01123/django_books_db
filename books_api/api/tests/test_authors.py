from multiprocessing import managers
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient
from api import serializers

from api.serializers import AuthorSerializer
from api.models import Author

AUTHORS_URL = reverse('authors-list')

def sample_author(first_name, last_name):
    Author.objects.create(first_name= first_name, last_name= last_name)

class PrivateAuthorsApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_list_authors(self):
        sample_author('javier','andrade')
        sample_author('benito','juarez')

        res = self.client.get(AUTHORS_URL)

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['results'], serializer.data)

