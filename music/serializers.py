from rest_framework import serializers
from .models import Album, Track


class TrackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('artist', 'title', 'duration')


class AlbumSerializer(serializers.ModelSerializer):
    album_tracks = TrackListSerializer(many=True, required=False)

    class Meta:
        model = Album
        fields = ('id', 'title', 'year', 'album_tracks')

    def create(self, validated_data):
        tracks_data = validated_data.pop('album_tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

    def update(self, instance, validated_data):
        tracks_data = validated_data.pop('album_tracks')
        tracks = instance.album_tracks.all()
        tracks = list(tracks)
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)
        instance.save()

        for track_data in tracks_data:
            track = tracks.pop(0)
            track.artist = track_data.get('artist', track.artist)
            track.title = track_data.get('title', track.title)
            track.duration = track_data.get('duration', track.duration)
            track.save()
        return instance


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
