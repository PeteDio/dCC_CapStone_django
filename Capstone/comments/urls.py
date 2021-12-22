from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.CommentsList.as_view()),
    path('comments/<int:pk>/', views.CommentsDetail.as_view()),
     path('mealid/<int:post>/', views.CommentsByMealId.as_view()),
]