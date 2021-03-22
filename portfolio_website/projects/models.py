from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=60)
    image = models.ImageField(upload_to="../static/projects/images")
    link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

