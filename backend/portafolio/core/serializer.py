from django.conf import settings
from .models import Album, Home, Image, Video
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'picture','thumbnail')


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('id', 'name', 'coveralbum','images')

    def get_images(self, obj):
            image_ids = obj.images.values_list('id', flat=True)
            images = Image.objects.filter(id__in=image_ids)
            return[{'id':t.id,'name':t.name,'picture':t.picture.url,'description':t.description,'thumbnail':t.thumbnail.url} for t in images]



class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
