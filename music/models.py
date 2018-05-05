from django.db import models


# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=140)
    year = models.SmallIntegerField()

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    artist = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    duration = models.DurationField()

    def __str__(self):
        return self.title
