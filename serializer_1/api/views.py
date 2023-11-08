'''
1. database - create class
2. admin - register
3. create serializers.py 
    - import serializer
    - create class
4. views.py
5. urls.py
'''


from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Ex-01
# Model objects - single student data

def student_details(request):
    stu = Student.objects.get(id=1)      #complex data 
    
    # Python data convert from complex data
    serializer = StudentSerializers(stu)        # convert python Ex: variable(obj)_name = serilizer_class_name(complex data)    
    
    # Json data convert from  python data
    json_data = JSONRenderer().render(serializer.data)  #convert Json Ex: variable(obj)_name = JSONRenderer().render(python_convert.data)
    
    
    return HttpResponse(json_data, content_type = 'application/json') #passing client-HttpResponse(json_convert, content_type ='application/json')


#Ex-02
# Model Objects - Single student data with one-by-one primary keys

def student_details_pk(request, pk):
    stu = Student.objects.get(id=pk)      # initial primary key
    serializer = StudentSerializers(stu)
    json_data = JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type = 'application/json')


#Ex-03
#QuerySet - all student data 

def student_list(request):
    stu = Student.objects.all() 
    serializer = StudentSerializers(stu, many=True)     # All data is displayed if the condition is True
    json_data = JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type = 'application/json')

