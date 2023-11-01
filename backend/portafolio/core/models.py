from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    cover = models.ImageField(upload_to="images/")


def __str__(self):
    return self.title


class Album(models.Model):
    title = models.CharField(max_length=100)
    coveralbum = models.ImageField(upload_to="images/",blank=True)


def __str__(self):
    return self.title


class Image(models.Model):
    album=models.ManyToManyField('Album',related_name='images') 
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    thumbnai= models.ImageField(upload_to="images/",blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos/")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
