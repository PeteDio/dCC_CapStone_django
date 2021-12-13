from django.http import request
from django.urls import path
from meals import views


urlpatterns = [
    path('all/', views.get_all_meals),
    path('', views.user_meals),

]