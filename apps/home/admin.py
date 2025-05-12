from django.contrib import admin
from apps.home import models

admin.site.register(models.Album)
admin.site.register(models.Track)
