from django.shortcuts import render
from accounts.models import User
from rest_framework import viewsets, generics
from api.serializers import UserSerializer
from rest_framework.views import APIView

# Create your views here.


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(APIView):
    def post(request):
        username = request.data['username']
        password = request.data['password']

        return ({'username': username})


class LogoutView(APIView):
    def post(request):
        pass

class RegisterView(APIView):
    def post(request):
        pass


