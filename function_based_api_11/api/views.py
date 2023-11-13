from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])      # get, post, put, patch, delete
def hello_world(request):       # function based api
    
    if request.method == 'GET':                              # get request
        return Response({'msg': 'This is GET Request'})

    
    if request.method == 'POST':                             # post request
        return Response({'msg': 'This is Post Request', "data": request.data})