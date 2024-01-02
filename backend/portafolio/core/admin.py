from django.contrib import admin
from .models import Album,Image,Home,Video,About
# Register your models here.


admin.site.register(Home)
admin.site.register(Album)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(About)

