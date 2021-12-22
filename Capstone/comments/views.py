from django.shortcuts import render
from .models import Comment
from .serializers import CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

# Create your views here.


class CommentsList(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        permission_classes = [IsAuthenticated]
        if permission_classes == [IsAuthenticated]:
            serializer = CommentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    # get by id
    def get(self, request, pk): # 1, 2, 3 
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)


  

    # update
    def put(self, request, pk):
        permission_classes = [IsAuthenticated]
        if permission_classes == [IsAuthenticated]:
            comments = self.get_object(pk)
            serializer = CommentsSerializer(comments, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        permission_classes = [IsAuthenticated]
        if permission_classes == [IsAuthenticated]:
            comments = self.get_object(pk)
            comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentsByMealId(APIView):


    def get_objects_by_post_id(self, post):
        try:
            return Comment.objects.filter(post = post)
        except Comment.DoesNotExist:
            raise Http404


    def get(self, request, post):

        permission_classes = [IsAuthenticated]
        if permission_classes == [IsAuthenticated]:
            comments = self.get_objects_by_post_id(post)
            serializer = CommentsSerializer(comments, many=True)
            return Response(serializer.data)
        