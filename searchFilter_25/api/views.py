from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentModelSerializer

from rest_framework.filters import SearchFilter

# Create your views here.
# http://127.0.0.1:8000/studentapi/?search=Liza

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    filter_backends = [SearchFilter]
    # search_fields = ['name']              # search_fields = []
    search_fields = ['^name']           # '^' Starts-with search first letter, '=' Exact matches, '$' Regex search
    # search_fields = ['name', 'city']



