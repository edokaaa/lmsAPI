from rest_framework import serializers
from lms.models import Track, Course, Tag

from django.utils.text import slugify

# from accounts.serializers import UserMiniSerializer
from accounts.models import User



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
    tutor_id = serializers.IntegerField(write_only=True)
    # duration = serializers.SerializerMethodField()
    # duration = serializers.SerializerMethodField(read_only=True)
    # track = TrackSerializer(read_only=True)
    # tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'duration', 'slug', 'tutor_id', 'location', 'price', 
        'track', #'tags',
        ]
    
    def create(self, validated_data):
        tutor_id = validated_data.pop('tutor_id')
        tutor = User.objects.get(id=tutor_id)
        validated_data = {
            **{
                "tutor": tutor
            },
            **validated_data
        }

        return Course.objects.create(**validated_data)

    def get_tutor_id(self, obj):
        return obj.tutor.id

    # def get_duration(self, obj):
    #     return f"{obj.duration} weeks"

    def get_slug(self, obj):
        # if hasattr(obj, 'slug'):
        #     return obj.slug
        return obj.slug



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
