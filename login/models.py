from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Usuarios(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    instrumento = models.CharField(max_length=50)
    #id_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_nacimiento = models.DateField()
    date_created = models.DateField()

    def __str__(self):
        return self.firstname+' '+self.lastname
