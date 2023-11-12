from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):               # define ModelSerializer
    # Ex-01
    # name = serializers.CharField(read_only=True)                  # Choose any of your options in writing (ex-01 / ex-02)
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        
        # Ex-02
        read_only_fields = ['name', 'roll']