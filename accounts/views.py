from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from django.http import JsonResponse
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import StudentSerializer, TutorSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = User.objects.all()


class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    queryset = User.objects.all()
