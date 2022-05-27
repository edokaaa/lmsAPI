from rest_framework import viewsets, generics
from api.serializers import CapstoneProjectSerializer, CourseMaterialSerializer, TrackSerializer, UserSerializer, CourseSerializer
from lms.models import CapstoneProject, Track, User, Course, CourseMaterial

# Create your views here.




class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseMaterialView(viewsets.ModelViewSet):
    serializer_class = CourseMaterialSerializer
    queryset = CourseMaterial.objects.all()

class TrackView(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class TrackDetailAPIView(generics.RetrieveAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class CapstoneProjectView(viewsets.ModelViewSet):
    serializer_class = CapstoneProjectSerializer
    queryset = CapstoneProject.objects.all()


class CapstoneDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CapstoneProjectSerializer
    queryset = CapstoneProject.objects.all()
