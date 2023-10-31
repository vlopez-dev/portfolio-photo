from django.db import models

# Create your models here.

class Home(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    




    
class Album(models.Model):
    title=models.CharField(max_length=100)
    
def __str__(self):
                return self.title



class Image(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    description=models.TextField(blank=True)
    
    
    def __str__(self):
                return self.title

    