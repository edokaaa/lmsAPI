from rest_framework import serializers
from lms.models import Track, Course, Tag

from django.utils.text import slugify

from accounts.serializers import UserMiniSerializer



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class TrackSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Track
        fields = ('id', 'name', 'description', 'slug')
    
    def get_slug(self, obj):
        if hasattr(obj, 'slug'):
            return obj.slug
        return slugify(obj.name)


class CourseSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)
    tutor = UserMiniSerializer(read_only=True)
    duration = serializers.SerializerMethodField(read_only=True)
    # duration = serializers.SerializerMethodField(read_only=True)
    # track = TrackSerializer(read_only=True)
    # tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'duration', 'slug', 'tutor', 'location'
        # 'track', 'tags',
        ]
        

    def get_duration(self, obj):
        return f"{obj.duration} weeks"

    def get_slug(self, obj):
        if hasattr(obj, 'slug'):
            return obj.slug
        return slugify(obj.name)



# class CourseMaterialSerializer(serializers.ModelSerializer):
#     material_type = serializers.SerializerMethodField(read_only=True)
#     # url = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = CourseMaterial
#         fields = ('id', 'title', 'description', 'course_id', 'material_type')
    
#     def get_material_type(self, obj):
#         return obj.get_type
    

# class CapstoneProjectSerializer(serializers.ModelSerializer):
#     course = CourseSerializer(read_only=True)
#     class Meta:
#         model = CapstoneProject
#         fields = ('id', 'title', 'course')


# class VoucherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Voucher
#         fields = ('id', 'code', 'percentage', 'is_used')
