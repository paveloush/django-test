from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from .serializers import TrackSerializer, AlbumSerializer
from .models import Track, Album


class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    renderer_classes = (JSONRenderer, )


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    renderer_classes = (JSONRenderer, )


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    renderer_classes = (JSONRenderer, )


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    renderer_classes = (JSONRenderer, )
