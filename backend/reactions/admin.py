from django.contrib import admin

# Register your models here.
from .models import Category, Reaction

admin.site.register(Category)
admin.site.register(Reaction)