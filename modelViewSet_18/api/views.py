from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentModelSerializer

# Ex-01
class StudentModelViewSet(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer




# Ex-02
# class StudentReadOnlyModerViewSet(viewsets.ReadOnlyModelViewSet):
    
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
