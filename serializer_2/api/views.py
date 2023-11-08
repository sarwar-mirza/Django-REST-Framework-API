from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse


# Model Object - singel student data
'''
def student_details(request, pk):
    stu = Student.objects.get(id=pk)   # complex data
    serializer = StudentSerializer(stu)  # python convert from complex data
    json_data = JSONRenderer().render(serializer.data)  # json convert from python data
    
    return HttpResponse(json_data, content_type = 'application/json') # passing client
    '''
    
def student_details(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    
    return JsonResponse(serializer.data)



# QuerySet - all student data

def student_list(request):
    stu = Student.objects.all()
    serilizer = StudentSerializer(stu, many = True)
    
    return JsonResponse(serilizer.data, safe=False)       # By Default safe=True, all data showing you can write safe=False
    
    
