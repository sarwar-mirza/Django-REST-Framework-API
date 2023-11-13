from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentModelSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    
    # Request the GET() method on the task
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentModelSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many=True)
        return Response(serializer.data)
    
    # Request the POST() method on the task
    if request.method == 'POST':
        serializer = StudentModelSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Your data is inserted'}
            return Response(response_msg, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # Request the PUT() method on the task
    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudentModelSerializer(stu, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Completley Your data is updated '}
            return Response(response_msg, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # Request the PATCH() method on the task
    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudentModelSerializer(stu, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Partial Your data is updated '}
            return Response(response_msg)
        
        return Response(serializer.errors)
    
    
    
    # Request the DELETE() method on the task
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(id = id)
        stu.delete()
            
        response_msg = {'msg': 'your data is deleted'}
        return Response(response_msg)
        
    
