from django.shortcuts import render
# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView # ex-01


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView   # ex-02
from .models import Student
from .serializers import StudentModelSerializer

# Create your views here.
'''
# ex-01
class StudentListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    
class StudentCreateApi(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentRetrieveApi(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentUpdateApi(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
class StudentDestroyApi(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

'''

# ex -02
# note- It provides GET and POST method handlers
class StudentListCreateApiView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

# note- It provides GET, UPDATE and DELETE method handlers
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


