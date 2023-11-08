'''
step by step
1. create model class
2. create admin class
3. create serializer.py
    - import rest_framework
    - create class
        - create function
4. create myapp.py (note-Desktop or python or java or user application), Do not api this part
    - import requests, json
    - hard python code (data)
    - python-to-json convert using dumps() method
    - post request
    - object (->json()method)

5. views.py hard code
6. urls.py
'''


from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']


