from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default="Sin título")
    description = models.TextField()
    image =models.ImageField(upload_to='blog/images')
    date = models.DateField()