from rest_framework import serializers
from .models import Track, Album

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')

        rep['album'] = instance.album.title if instance.album else None

        if request:
            if instance.cover:
                rep['cover'] = request.build_absolute_uri(instance.cover.url)
            if instance.audio_file:
                rep['audio_file'] = request.build_absolute_uri(instance.audio_file.url)

        return rep


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

