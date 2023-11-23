from rest_framework import serializers
from enroll.models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'department', 'city', 'email', 'password']


