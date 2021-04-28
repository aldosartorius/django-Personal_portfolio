from django.contrib import admin

# import my models
from .models import Blog

# Register your models here.
admin.site.register(Blog)
