from django.db import models

# Create your models here.

class people_details(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    city = models.CharField(max_length = 100)
    show = models.IntegerField()