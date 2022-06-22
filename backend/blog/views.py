from django.shortcuts import render
from .models import Posts
from rest_framework import generics
from .serializer import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


