from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artists/", views.artists, name="artists"),
    path("releases/", views.releases, name="releases"),
    path("contact/", views.contact, name="contact"),
]
