from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug= models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
