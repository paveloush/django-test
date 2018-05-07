from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=140)
    year = models.SmallIntegerField()

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_tracks', blank=True, null=True)
    artist = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    duration = models.DurationField()

    def __str__(self):
        return self.title
