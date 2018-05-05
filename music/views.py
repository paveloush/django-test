from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Album, Track
from .serializers import *


class TrackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Track.objects.all().order_by('title')
    serializer_class = TrackSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer