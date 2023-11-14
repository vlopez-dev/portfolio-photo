from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    cover = models.ImageField(upload_to="media/")


def __str__(self):
    return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    coveralbum = models.ImageField(upload_to="media/",blank=True)


    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="media/")
    thumbnail= models.ImageField(upload_to="media/",blank=True)
    description = models.TextField(blank=True)
    album=models.ManyToManyField('Album',related_name='images') 

    def __str__(self):
        return self.name


class Video(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to="media/")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
