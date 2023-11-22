from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentModelSerializer

from .mypaginations import MyCursorPagination



class StudentListApiView(ListAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    pagination_class = MyCursorPagination


