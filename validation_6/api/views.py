from django.shortcuts import render
from django.views.generic.base import View
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentApiView(View):
    # Request the get() method on the task
    def get(self, request, *args, **kwargs):
        json_data = request.body                   # json data
        stream = io.BytesIO(json_data)             # stream data convert from json data
        python_data = JSONParser().parse(stream)   # python data convert from stream
        
        id = python_data.get('id', None) 
        
        if id is not None:
            stu = Student.objects.get(id= id)        # complex data
            serializer = StudentSerializer(stu)      # python data
            
            return JsonResponse(serializer.data, safe=False)  # json data
        
        stu = Student.objects.all()                      # complex data
        serializer = StudentSerializer(stu, many= True)  # python data
        return JsonResponse(serializer.data, safe=False) # json data
    
    
    
    # Request the post() method on the task
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data= python_data)
        
        if serializer.is_valid():                            # condition check Field level validation 
            serializer.save()
            
            response_msg = {'msg': 'Your Data is created'}
            return JsonResponse(response_msg, safe= False)
        
        return JsonResponse(serializer.errors, safe=False)


    
    # Request the put() method on the task
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id')
        
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data= python_data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Your data is Updated'}
            return JsonResponse(response_msg, safe=False)
        
        return JsonResponse(serializer.errors, safe= False)
    
    
    
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


