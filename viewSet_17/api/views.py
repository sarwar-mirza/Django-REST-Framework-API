from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentModelSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentModelSerializer(stu)
            return Response(serializer.data)
    
    
    def create(self, request):
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_msg={'msg': 'Your data is Created'}
            return Response(response_msg, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def update(self, request, pk):
        id = pk
       
        stu = Student.objects.get(id = id)
        serializer = StudentModelSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_msg ={'msg': 'Complete Your data is Updated'}
            return Response(response_msg, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    
    def partial_update(self, request, pk):
        id = pk
       
        stu = Student.objects.get(id = id)
        serializer = StudentModelSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_msg ={'msg': 'Partial Your data is Updated'}
            return Response(response_msg, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    
    def delete(self, request, pk):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        response_msg = {'msg': 'Your data is deleted'}
        return Response(response_msg)
    
