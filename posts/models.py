from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug= models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.title