from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to Archaic Revival Records")


def artists(request):
    return HttpResponse("You're at the Artists page")


def releases(request):
    return HttpResponse("You're at the Releases page")
