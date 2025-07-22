from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    year = models.IntegerField()
    stream = models.IntegerField()

    def __str__(self):
        return self.title