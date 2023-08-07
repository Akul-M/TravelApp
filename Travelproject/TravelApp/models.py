from django.db import models

# Create your models here.

class Destinations(models.Model):
    place = models.CharField(max_length=250)
    img = models.ImageField(upload_to='Pics')
    description = models.TextField()

    def __str__(self):
        return self.place


class Teams(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='Pics')
    description = models.TextField()

    def __str__(self):
        return self.name