from django.conf import settings
from .models import Album, Home,Image,Video
from rest_framework import serializers



class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        
        
        
        
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        
        
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        
        
        
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'