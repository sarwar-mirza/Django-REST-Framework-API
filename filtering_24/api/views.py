from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentModelSerializer

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


'''
# EX-01(global filter)
class StudentListAPIView(ListAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)

'''


# EX-02 (per view filter)
class StudentListAPIView(ListAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    filter_backends = [DjangoFilterBackend]        # per view filter    
    filterset_fields = ['city', 'name']




    
    
