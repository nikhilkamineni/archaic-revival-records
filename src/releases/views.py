from django.http import HttpResponse
from django.shortcuts import render

from .models import Artist, Release


def index(request):
    return render(request, "releases/index.html")


def artists(request):
    artists = Artist.objects.all()
    context = {"artists": artists}

    return render(request, "releases/artists.html", context)


def releases(request):
    releases = Release.objects.all()
    context = {"releases": releases}

    return render(request, "releases/releases.html", context)
