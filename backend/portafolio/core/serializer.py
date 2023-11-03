from django.conf import settings
from .models import Album, Home, Image, Video
from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('id', 'title', 'coveralbum','images')

    def get_images(self, obj):
            images_ids = obj.images.values_list('id', flat=True)
            images = Image.objects.filter(id__in=images_ids)
            return [{'id': i.id, 'image': i.image,'thumbnai':i.thumbnai} for i in images]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
