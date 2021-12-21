from rest_framework import serializers
from .models import Replies


class RepliesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ['comments_id', 'comments', 'text','userId']
