from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentModelSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentModelViewSetView(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    authentication_classes = [TokenAuthentication]     # Authentication
    permission_classes = [IsAuthenticated]             # permission
    
    
    
    
    '''
    1st- any command prompt open
    2nd- without authentication and permission for rest_framework, http http://127.0.0.1:8000/urls
                    Ex- http http://127.0.0.1:8000/studentapi/   
    
    1st- any command prompt open
    2nd- with atuthentication and permission for rest_framework, http http://127.0.0.1:8000/studentapi/'Authorization:Token create_token_serial_number'
                    Ex- http http://127.0.0.1:8000/studentapi/ 'Authorization:Token 5c8aea9fe205e5759cdedbea6058de229898c093'
    
    1st - any command prompt open
    2nd - with atuthentication and permission for (POST,PUT,DELETE)rest_framework, 
        Ex-
        post->    http -f POST http://127.0.0.1:8000/studentapi/ name=sarwar roll=104 city=Noakhali'Authorization:Token create_token_serial_number'
        put->     http PUT http://127.0.0.1:8000/studentapi/4/ name=mithu roll=104 city=Noakhali'Authorization:Token create_token_serial_number'
        delete->  http DELETE http://127.0.0.1:8000/studentapi/4/ 'Authorization:Token create_token_serial_number'
    '''
    
