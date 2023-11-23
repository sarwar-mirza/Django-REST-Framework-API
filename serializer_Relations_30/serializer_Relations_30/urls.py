
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api import views

# Create Router
router = DefaultRouter()

# Register SingerModelViewSet, SongModelViewSet with router
router.register('singerapi', views.SingerModelViewSet, basename='singer_base')
router.register('songsapi', views.SongsModelViewSet, basename='song_base')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
