from rest_framework import serializers
from .models import Student


# validators Field validation, Type-03
def start_with_s(value):
    if value[0].lower()  != 's':
        raise serializers.ValidationError('Name should be start with S')
    

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators=[start_with_s])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        
        instance.save()
        return instance
    
    
    # Field level validation, Type -01
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Oops ! Seat Full, Better then next time try again')
        return value
    
    # Object level validation,  Type-02
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        
        if nm.lower() == 'sarwar' and ct.lower() != 'noakhali':
            raise serializers.ValidationError('City must be Noakhali')
        return data