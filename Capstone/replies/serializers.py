from rest_framework import serializers
from .models import Reply


class RepliesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['comments_id', 'comments', 'text','userId']
