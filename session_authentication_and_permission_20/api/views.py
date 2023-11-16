from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentModelSerializer

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    authentication_classes = [SessionAuthentication]    # session authentication
    
    # permission_classes = [IsAuthenticated]              # IsAuthenticated means all users have access to the registry
    
    # permission_classes = [IsAdminUser]                    # IsAdminUser means is_staff users have access to the registry
    # permission_classes = [IsAuthenticatedOrReadOnly]       # IsAuthenticatedOrReadOnly means random user read only and IsAuthenticatedOrReadOnly
    
    # permission_classes = [DjangoModelPermissions]          # Django model permissions- change, delete, view, add
    
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # Django modelr mermissions and unauthorized user Only read
    