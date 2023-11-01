from django.shortcuts import render
from rest_framework import viewsets
from .serializer import AlbumSerializer, HomeSerializer, VideoSerializer
from .models import Album, Home
from django.shortcuts import get_object_or_404
from urllib import response

# Create your views here.


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = HomeSerializer
    template_name='core/index.html'
    
    
    
    def get(self, request, id):
        home = get_object_or_404(Home, pk=id)
        serializer = HomeSerializer(home)
        print(serializer)
        return response({'serializer': serializer, 'home': home},template_name='index.html')
