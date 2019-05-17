from django.db import models

# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=20, default='nan')
    lastname = models.CharField(max_length=20, default='nan')
    confirmation = models.BooleanField(default=False)
    born_date = models.DateField(null=True)
    sex = models.CharField(max_length=10, default='nan')
    email = models.CharField(max_length=20, default='nan')
    password = models.CharField(max_length=20, default='nan')
    
    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)