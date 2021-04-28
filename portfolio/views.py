from django.shortcuts import render
# import my database
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

# Create your views here.
