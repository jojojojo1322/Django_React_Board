#backend/post/serializers.py

from rest_framework import serializers
from .models import Post
from umc.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id','nickname',"email")

class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)