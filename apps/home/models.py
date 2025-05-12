from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers/')

    def __str__(self):
        return f"{self.title} — {self.artist}"

class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='tracks/')
    cover = models.ImageField(upload_to='covers/')
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, related_name="tracks")

    def __str__(self):
        return f"{self.title} — {self.artist}"