from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    power_level = models.CharField(max_length=32)
    transformation = models.CharField(max_length=32)