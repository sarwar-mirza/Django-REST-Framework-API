'''
Note - Serializer(complex data -> python Data -> json data)
    - De-serializer(json data -> python Data -> complex data)
'''

from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body  # Receive information sent by the user(Desktop,python application)
        stream = io.BytesIO(json_data) # stream data convert from json(receive) data
        python_data = JSONParser().parse(stream) # python data convert from stream data using JSONParser()
        serializer = StudentSerializer(data=python_data) # complex data convert from python_data
        
        if serializer.is_valid():
            serializer.save()
            
            response_msg = {'msg': 'Data Created Successfully'}    # python data
            
            json_msg_data = JSONRenderer().render(response_msg)                   # json data
            return HttpResponse(json_msg_data, content_type = 'application/json')
        
        json_msg_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_msg_data, content_type = 'application/json')

