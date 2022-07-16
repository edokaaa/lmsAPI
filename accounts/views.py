from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.


# class UserView(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


# class UserDetailAPIView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


class StudentDetailAPIView():
    pass


class TutorDetailAPIView():
    pass

class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        return Response({"username": username})


class LogoutView(APIView):
    def post(self, request):
        pass


class RegisterView(APIView):
    def post(self, request):
        pass
