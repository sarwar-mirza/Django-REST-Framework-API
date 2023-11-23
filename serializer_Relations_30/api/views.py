from django.shortcuts import render
from rest_framework import viewsets
from .models import Singer, Songs
from .serializers import SingerModelSerializer, SongsModelSerializer

# Create your views here.
class SingerModelViewSet(viewsets.ModelViewSet):
    
    queryset = Singer.objects.all()
    serializer_class = SingerModelSerializer


class SongsModelViewSet(viewsets.ModelViewSet):
    
    queryset = Songs.objects.all()
    serializer_class = SongsModelSerializer




