from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentModelSerializer

from rest_framework.filters import OrderingFilter

# Create your views here.
# http://127.0.0.1:8000/studentapi/?ordering=name 

class StudentListApiView(ListAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    filter_backends = [OrderingFilter]    # Filter Ordering
    ordering_fields = ['name']            # specific ordering fields



