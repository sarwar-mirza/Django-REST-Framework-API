from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentModelSerializer
from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPIview(APIView):
    
    # Request the GET() method on the task
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentModelSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many=True)
        return Response(serializer.data)
    
    
    # Request the POST() method on the task
    def post(self, request, format=None):
        serializer = StudentModelSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Your data is inserted'}
            return Response(response_msg, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # Request the PUT() method on the task
    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudentModelSerializer(stu, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Completley Your data is updated '}
            return Response(response_msg, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    # Request the PATCH() method on the task
    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudentModelSerializer(stu, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Partial Your data is updated '}
            return Response(response_msg, status=status.HTTP_206_PARTIAL_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    # Request the DELETE() method on the task
    def delete(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(id = id)
        stu.delete()
            
        response_msg = {'msg': 'your data is deleted'}
        return Response(response_msg, status=status.HTTP_404_NOT_FOUND)
    
    
    
    

        
        
    
