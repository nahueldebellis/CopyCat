from django.db import models
# Create your models here.

class Song(object):
    name = models.CharField(max_length=30)
    duration = models.BigIntegerField(max_length=4)
    author = models.CharField(max_length=30)
    year = models.BigIntegerField(max_length=4)
    path = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
