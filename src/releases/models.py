from django.db import models
from uuid import uuid4


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    genre = models.CharField(max_length=100)
    # TODO: Image link


class Release(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    year = models.IntegerField(blank=True)
    # TODO: Streaming link
    # TODO: Artwork link
    # TODO: Tracklist
