from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer
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

class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
