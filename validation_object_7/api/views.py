from django.shortcuts import render
from django.views.generic.base import View
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentApiView(View):
    # Request the get() method on the task
    def get(self, request, *args, **kwargs):
        
        json_data = request.body            # json data
        stream =  io.BytesIO(json_data)         # stream data convert from json data
        python_data = JSONParser().parse(stream)  # python data convert from stream data
        
        id = python_data.get('id', None)
        
        if id is not None:
            stu = Student.objects.get(id = id)       # complex data
            serializer = StudentSerializer(stu)     # python data
            return JsonResponse(serializer.data, safe=False)  # json data
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return JsonResponse(serializer.data, safe=False)
    
    
    # Request the post() method on the task
    def post(self, request, *args, **kwargs):
        
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data= python_data)
        
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg': 'Your Data is Inserted successfully'}
            return JsonResponse(response_msg, safe=False)
            
        return JsonResponse(serializer.errors, safe=False)
    
    # Request the put() method on the task
    def put(self, request, *args, **kwargs):
        
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        serailizer = StudentSerializer(stu, data= python_data, partial= True)
        
        if serailizer.is_valid():
            serailizer.save()
            
            response_msg = {'msg': 'Your data is updated'}
            return JsonResponse(response_msg, safe=False)
        return JsonResponse(serailizer.errors, safe=False)
    
    
    # Request the delete() method on the task
    def delete(self, request, *args, **kwargs):
        
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id')
        
        stu = Student.objects.get(id = id)
        stu.delete()
        
        response_msg = {'msg': 'Your data is deleted'}
        return JsonResponse(response_msg, safe=False)
    
