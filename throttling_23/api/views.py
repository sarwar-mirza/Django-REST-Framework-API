from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentModelSerializer

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.throttling import AnonRateThrottle  # ,UserRateThrottle  # EX-01

from .throttling import MithuRateThrottle   # EX-02


# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]       # EX-01
    
    throttle_classes = [AnonRateThrottle, MithuRateThrottle]        # EX-02



