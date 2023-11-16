from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentModelSerializer

from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated

from .custompermissions import Mypermission              # create custom permission import

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    authentication_classes = [SessionAuthentication]
    
    # permission_classes = [IsAuthenticated]                     # IsAuthenticated means all users have access to the registry
    
    permission_classes = [Mypermission]                # custom permission
