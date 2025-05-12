from django.contrib import admin
from apps.home import models
# Register your models here.

admin.site.register(models.Album)
admin.site.register(models.Track)
