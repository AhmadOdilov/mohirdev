from django.db import models
class Post(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE())
# Create your models here.

