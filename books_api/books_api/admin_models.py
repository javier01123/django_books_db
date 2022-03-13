from django.contrib import admin
from api.models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
