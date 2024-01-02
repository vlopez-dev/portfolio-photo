from django.conf import settings
from .models import About, Album, Home, Image, Video
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
        request = self.context.get('request')
        image_ids = obj.images.values_list('id', flat=True)
        images = Image.objects.filter(id__in=image_ids)
        image_data = []
        for image in images:
            image_data.append({
                'id': image.id,
                'name': image.name,
                'picture': request.build_absolute_uri(image.picture.url) if request else image.picture.url,
                'description': image.description,
                'thumbnail': request.build_absolute_uri(image.thumbnail.url) if request else image.thumbnail.url,
            })
        return image_data
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"



class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"
