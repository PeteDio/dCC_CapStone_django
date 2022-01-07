from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class GetUserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class EditUser(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        user = self.get_object(pk)
        if user == None:
            print("error finding user")

        user.username = request.data["username"]
        user.password = request.data["password"]
        user.email = request.data["email"]
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.middle_name = request.data["middle_name"]
        
        serializer = UserSerializer(user)
        user.save()

        return Response(serializer.data)