from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from lms.models import CapstoneProject, CourseMaterial, Track, User, Course, Voucher

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = (User)
        fields = ('id', 'username', 'first_name', 'last_name', 'user_type')


class CourseSerializer(serializers.ModelSerializer):
    course_duration = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'tutor_id', 'price', 'course_duration')
    

    def get_course_duration(self, obj):
        return obj.get_duration

class CourseMaterialSerializer(serializers.ModelSerializer):
    material_type = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CourseMaterial
        fields = ('id', 'title', 'description', 'course_id', 'material_type')
    
    def get_material_type(self, obj):
        return obj.get_type
    

class TrackSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Track
        fields = ('id', 'description', 'courses')


class CapstoneProjectSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = CapstoneProject
        fields = ('id', 'title', 'course')


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ('id', 'code', 'percentage', 'is_used')
