from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseVideoSerializer, UserSerializer, CourseSerializer
from .models import User, Course, CourseVideo

# Create your views here.


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseVideoView(viewsets.ModelViewSet):
    serializer_class = CourseVideoSerializer
    queryset = CourseVideo.objects.all()