from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentModelSerializer
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    
    # Request the get() method on the task
    if request.method == 'GET':
        id = request.data.get('id')                  # request.data = all data information
        
        if id is not None:
            # Model object - single student
            stu = Student.objects.get(id = id)
            serializer = StudentModelSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many=True)
        return Response(serializer.data)
    
    
    # Request the post() method on the task
    if request.method == 'POST':
        serializer = StudentModelSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Your data is inserted'}
            return Response(response_msg)
        return Response(serializer.errors)
    
    
    # Request the put() method on the task
    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        
        serializer = StudentModelSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Your data is updated'}
            return Response(response_msg)
        return Response(response_msg)
    
    # Request the delete() method on the task 
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        
        stu.delete()
        response_msg = {'msg': 'Your data is deleted'}
        return Response(response_msg)

