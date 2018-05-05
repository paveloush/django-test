from django.contrib import admin

# Register your models here.
from .models import *


# class TrackAdmin(admin.ModelAdmin):
#     class Meta():
#         model = Track
#
#
# class AlbumAdmin(admin.ModelAdmin):
#     class Meta():
#         model = Album

admin.site.register(Track)
admin.site.register(Album)