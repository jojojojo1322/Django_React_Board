#backend/post/views.py
# from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, status
from rest_framework.views import APIView
# from rest_framework.decorators import api_view

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from rest_framework.permissions import IsAuthenticated



class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentList(APIView):

    def post(self, request, pk, format=None):
        serializer = CommentSerializer(data=request.data)
        print(request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save(post=Post.objects.get(pk=pk), user=request.user)
            print("success")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        queryset = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)

class CommentDetail(APIView):
    def get_object(self, post_pk, comment_pk):
        try:
            return Comment.objects.get(post_id=post_pk, pk=comment_pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, post_pk, comment_pk):
        comment = self.get_object(post_pk, comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, post_pk, comment_pk, format=None):
        comment = self.get_object(post_pk, comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk, comment_pk, format=None):
        comment = self.get_object(post_pk, comment_pk)
        comment.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

