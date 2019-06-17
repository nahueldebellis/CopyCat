from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=30)
    duration = models.BigIntegerField()
    author = models.CharField(max_length=30)
    album = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    year = models.BigIntegerField()
    path = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.name, self.author)