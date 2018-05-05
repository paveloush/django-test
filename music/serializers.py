from datetime import datetime
from rest_framework import serializers
from .models import Album, Track


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'year', 'tracks')


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
