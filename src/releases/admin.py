from django.contrib import admin
from .models import Artist, Release

admin.site.register((Artist, Release))
