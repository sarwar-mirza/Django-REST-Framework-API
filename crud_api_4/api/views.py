'''
Note: Serializer- (complex data -> python data -> json data)
      De-Serializer - (json data -> python data -> complex data)
'''

from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Request the get() method on the task
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body 
        stream = io.BytesIO(json_data)   # stream data convert from json data
        python_data = JSONParser().parse(stream)  # python data convert from stream
        
        id = python_data.get('id', None)
        
        if id is not None:
            # Model objects - single student data
            
            stu = Student.objects.get(id = id)                  # complex data
            serializer = StudentSerializer(stu)      # python data convert from complex data
            pythondata = JSONRenderer().render(serializer.data) # json data convert from python data 
            
            return HttpResponse(pythondata, content_type = 'application/json')    # passing client
        
        
        # QuerySet - all student data
        
        stu = Student.objects.all()                    # complex data
        serializer = StudentSerializer(stu, many=True)    # python data
        pythondata = JSONRenderer().render(serializer.data)   # json data
        
        return HttpResponse(pythondata, content_type = 'application/json')
    
    
    # *************************************************************************************************
    # Request the post() method on the task
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)               # json data
        python_data = JSONParser().parse(stream)          # python data
        serializer = StudentSerializer(data= python_data)  # complex data
        
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Your data created successfully'}
            json_msg_data = JSONRenderer().render(response_msg)
            return HttpResponse(json_msg_data, content_type = 'application/json')
        
        json_msg_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_msg_data, content_type = 'application/json')
    
    
    
    #**************************************************************************************
    
    # Request the put() method on the task
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data= python_data, partial=True)  # partial - All data not required
        
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Your data updated successfully'}
            json_msg_data = JSONRenderer().render(response_msg)
            return HttpResponse(json_msg_data, content_type = 'application/json')

        json_msg_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_msg_data, content_type = 'application/json')
    #*****************************************************************************************
    
    
    # Request the delete() method on the task    
        
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        
        response_msg = {'msg': 'Your data Deleted'}
        json_msg_data = JSONRenderer().render(response_msg)
        return HttpResponse(json_msg_data, content_type = 'application/json')
