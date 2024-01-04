from django.urls import path,include
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static
from . import views


router = routers.DefaultRouter()
router.register(r'home', views.HomeViewSet)
router.register(r'album', views.AlbumViewSet)
router.register(r'about', views.AboutViewSet)
router.register(r'video', views.VideoViewSet)







urlpatterns = [
    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
