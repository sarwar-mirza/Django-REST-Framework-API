from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentModelSerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    authentication_classes = [BasicAuthentication]        # BasicAuthentication
    permission_classes = [IsAuthenticated]                # IsAuthenticated means all users have access to the registry
    
    # permission_classes = [IsAdminUser]                  # IsAdminUser means is_staff users have access to the registry
    
    