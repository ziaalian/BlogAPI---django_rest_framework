from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorReadOnly

class PostList(generics.ListCreateAPIView):
    # View Level permissions
   # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
   # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
