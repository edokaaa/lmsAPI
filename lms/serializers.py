from rest_framework import serializers
from lms.models import CapstoneProject, CourseMaterial, Track, Course, Voucher, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'name', 'description', 'slug')


class CourseSerializer(serializers.ModelSerializer):
    course_duration = serializers.SerializerMethodField(read_only=True)
    track = TrackSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'tutor_id', 'price', 'course_duration', 'track', 'slug', 'tags', 'location')
    

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
    

class CapstoneProjectSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = CapstoneProject
        fields = ('id', 'title', 'course')


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ('id', 'code', 'percentage', 'is_used')
