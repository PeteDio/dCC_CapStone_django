from rest_framework import serializers
from .models import FavMeal

class FavMealsSerializer (serializers.ModelSerializer):
    class Meta:
        model = FavMeal
        fields = ['recipe','label']