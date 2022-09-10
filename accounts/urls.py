from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('tutors', views.TutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
