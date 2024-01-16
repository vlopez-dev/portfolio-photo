from django.db import models
from django_resized import ResizedImageField


class Home(models.Model):
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    cover=ResizedImageField(size=[1920, 1080], quality=100, upload_to="media/", force_format='WEBP', blank=True)


    def __str__(self):
        return self.title


class Album(models.Model):
    name = models.CharField(max_length=100)
    coveralbum = ResizedImageField(size=[800, 600], quality=100, upload_to="media/", force_format='WEBP', blank=True)
    


    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    picture = ResizedImageField(size=[1920, 1080], quality=75, upload_to="media/", force_format='WEBP', blank=True)
    thumbnail= ResizedImageField(size=[350, 400], quality=75, upload_to="media/", crop=['middle', 'center'], force_format='WEBP', blank=True)
    description = models.TextField(blank=True)
    album=models.ManyToManyField('Album',related_name='images') 
    
    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to="media/")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class About(models.Model):

    name = models.CharField(max_length=50,blank=True)
    
    image = ResizedImageField(size=[1920, 1080], quality=75, upload_to="media/", force_format='WEBP', blank=True)
    title = models.CharField(max_length=50,blank=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name