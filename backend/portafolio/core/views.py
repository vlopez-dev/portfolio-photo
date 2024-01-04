from django.shortcuts import render
from rest_framework import viewsets
from .serializer import (
    AboutSerializer,
    AlbumSerializer,
    HomeSerializer,
    ImageSerializer,
    VideoSerializer,
)
from .models import About, Album, Home, Image,Video
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
    queryset = Album.objects.all().order_by('id')
    serializer_class = AlbumSerializer
    template_name = "core/index.html"

    def get(self, request, id):
        album = get_object_or_404(Album, pk=id)
        serializer = AlbumSerializer(album)
        return response(
            {"serializer": serializer, "album": album}, template_name="index.html"
        )



class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    template_name = "core/index.html"

    def get(self, request, id):
        about = get_object_or_404(About, pk=id)
        serializer = AboutSerializer(about)
        return response(
            {"serializer": serializer, "about": about}, template_name="index.html"
        )



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    template_name = "core/index.html"

    def get(self, request, id):
        video = get_object_or_404(Video, pk=id)
        serializer = VideoSerializer(video)
        return response(
            {"serializer": serializer, "video": video}, template_name="index.html"
        )