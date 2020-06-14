from django.contrib import admin
from .models import Category,Profile,Book
admin.site.register([Category,Book, Profile])
