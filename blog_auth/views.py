from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serilizers import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "successfully registered"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)  # 🔥 session created
            return Response({"message": "Logged in"})
        return Response({"error": "Invalid credentials"}, status=400)


class LogoutView(APIView):
    def post(self, request):
        logout(request)  # 🔥 session destroyed
        return Response({"message": "Logged out"})


class ProfileView(APIView):
    def get(self, request):
        user = request.user
        return Response({"username": user.username, "email": user.email})
