#backend/post/serializers.py

from rest_framework import serializers
# from umc.models import User
from django.contrib.auth.models import User

from .models import Post, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','nickname',"email")

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'content',
            'comments',
            'created_at',
        )
        read_only_fields = ('created_at',)
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'post',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)
