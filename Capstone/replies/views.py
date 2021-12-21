from django.shortcuts import render
from .models import Reply
from .serializers import RepliesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

# Create your views here.


class RepliesList(APIView):

    def get(self, request):
        replies = Reply.objects.all()
        serializer = RepliesSerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request):
        permission_classes = [IsAuthenticated]
        if permission_classes == [IsAuthenticated]:
            serializer = RepliesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RepliesDetail(APIView):

    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    # get by id
    def get(self, request, pk):
        Reply = self.get_object(pk)
        serializer = RepliesSerializer(Reply)
        return Response(serializer.data)

    # update
    def put(self, request, pk):
        permission_classes = [IsAuthenticated]
        if permission_classes == [IsAuthenticated]:
            Reply = self.get_object(pk)
            serializer = RepliesSerializer(Reply, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        permission_classes = [IsAuthenticated]
        if permission_classes == [IsAuthenticated]:
            Reply = self.get_object(pk)
            Reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RepliesByComment(APIView):
    
    def get_objects_by_comment(self, comments_id):
        try:
            return Reply.objects.filter(comments_id = comments_id)
        except Reply.DoesNotExist:
            raise Http404


    def get(self, request, comment_id):
        replies = self.get_objects_by_comment(comment_id)
        serializer = RepliesSerializer(replies, many=True)
        return Response(serializer.data)
