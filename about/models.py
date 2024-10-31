from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title
    
class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"