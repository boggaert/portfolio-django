from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields import URLField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=300)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
