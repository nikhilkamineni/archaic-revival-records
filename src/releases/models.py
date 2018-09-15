from django.db import models
from uuid import uuid4


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    genre = models.CharField(max_length=100, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Release(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    year = models.IntegerField(blank=True, null=True)
    artwork = models.ImageField(null=True, blank=True)
    streaming_url = models.URLField(null=True, blank=True)
    # TODO: Tracklist?

    def __str__(self):
        return f'{self.artist} - {self.title}'
