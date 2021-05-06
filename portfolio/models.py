from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'portfolio/images/')
    url = models.URLField(blank = True) #blank=True means if you wish to permit empty values in forms

    #this line allows to view in the data base the name of the projects
    #instand of object 1 or 2
    def __str__(self):
        return self.title
