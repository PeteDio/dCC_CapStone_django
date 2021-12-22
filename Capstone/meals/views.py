from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Meal
from .serializers import MealSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_meals(request):
    meals = Meal.objects.all() 
    serializer = MealSerializer(meals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_meals(request):
    if request.method == 'POST':
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    
    elif request.method =='GET':
        meals = Meal.objects.filter(user_id=request.user.id)
        serializer= MealSerializer(meals, many=True)
        return Response(serializer.data)




@api_view(['POST'])
@permission_classes([AllowAny])        
def post_user_meals(request):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)