from rest_framework import serializers
from .models import Singer, Songs

class SingerModelSerializer(serializers.ModelSerializer):
    
    gaan = serializers.StringRelatedField(many=True, read_only=True)               # showing string 
    # gaan = serializers.PrimaryKeyRelatedField(many=True, read_only=True)           # showing id
    # gaan = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')           # showing model attribute [title, duration]
    
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'gaan']
        
        
class SongsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id', 'title', 'singer', 'duration']
    
    