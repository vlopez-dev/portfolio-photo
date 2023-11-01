from django.shortcuts import render
from rest_framework import viewsets
from .serializer import (
    AlbumSerializer,
    HomeSerializer,
    ImageSerializer,
    VideoSerializer,
)
from .models import Album, Home, Image
from django.shortcuts import get_object_or_404
from urllib import response

# Create your views here.


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    template_name = "core/index.html"

    def get(self, request, id):
        home = get_object_or_404(Home, pk=id)
        serializer = HomeSerializer(home)
        return response(
            {"serializer": serializer, "home": home}, template_name="index.html"
        )


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    template_name = "core/index.html"

    def get(self, request, id):
        album = get_object_or_404(Album, pk=id)
        serializer = AlbumSerializer(album)
        return response(
            {"serializer": serializer, "album": album}, template_name="index.html"
        )


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    template_name = "core/index.html"
