from django.http import request
from django.urls import path
from meals import views


urlpatterns = [
    path('all/', views.get_all_meals),
    path('user/get/', views.get_user_meals),
    path('user/post', views.post_user_meals),
]