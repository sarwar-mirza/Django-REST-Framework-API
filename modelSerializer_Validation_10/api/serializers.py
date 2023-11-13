from rest_framework import serializers
from .models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    
    # validations Level validation
    def start_with_s(value):
        if value[0].lower() != 's':
            raise serializers.ValidationError('Name should be start S')
    
    name = serializers.CharField(validators=[start_with_s])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Oops! Seat full. Better then next time try agai.')
        return value
    
    # Object Level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        
        if nm.lower() == 'sarwar' and ct.lower() != 'noakhali':
            raise serializers.ValidationError('Name is a Sarwar and City must be Noakhali')
        return data
    
    
