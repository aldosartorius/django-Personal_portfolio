from django.contrib import admin

# import my models
from .models import Project

# Register your models here.
admin.site.register(Project)
