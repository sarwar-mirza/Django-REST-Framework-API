from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentModelSerializer

from .mypaginations import MyPageNumberPagination


'''
# Ex-01 (Globally setting.py in all pages)
class StudentListApiView(ListAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
 '''   


# Ex-02 (Per view page,[Create- mypaginations.py])

class StudentListApiView(ListAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    pagination_class = MyPageNumberPagination