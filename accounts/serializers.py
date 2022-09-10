from dataclasses import fields
from rest_framework import serializers
from .models import User


class UserMiniSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'phone_number')
    
    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
   

class TutorSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'phone_number')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'courses', 'track')