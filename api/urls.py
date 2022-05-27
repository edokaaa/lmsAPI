from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'lms'


# API Home Routes

router = routers.DefaultRouter()
router.register(r'courses', views.CourseView, 'courses')
router.register(r'users', views.UserView, 'users')
router.register(r'materials', views.CourseMaterialView, 'materials')
router.register(r'tracks', views.TrackView, 'tracks')
router.register(r'capstone-projects', views.CapstoneProjectView, 'capstone-projects')



urlpatterns = [
    path('', include(router.urls)),

    path('courses/<int:pk>/', views.CourseDetailAPIView.as_view(), name='course_detail'),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view(), name='user_detail'),
    path('tracks/<int:pk>/', views.TrackDetailAPIView.as_view(), name='track_detail'),
    path('capstone-projects/<int:pk>/', views.CapstoneDetailAPIView.as_view(), name='capstone_detail'),]
