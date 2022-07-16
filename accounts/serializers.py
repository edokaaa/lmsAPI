from dataclasses import fields
from rest_framework import serializers
from .models import Student, Tutor


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = (Tutor)
        fields = ('id', 'username', 'first_name', 'last_name', 'courses')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = (Student)
        fields = ('id', 'username', 'first_name', 'last_name', 'courses', 'track')