from operator import truediv
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return  '{} {}'.format(self.first_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.TextField()
    isbn = models.CharField(max_length=13, unique=True, null=True, default=None)
    authors = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return self.title