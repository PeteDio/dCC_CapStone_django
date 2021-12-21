from django.urls import path
from . import views

urlpatterns = [
    path('/all', views.CommentsList.as_view()),
    path('comments/<int:pk>/', views.CommentsDetail.as_view()),
]