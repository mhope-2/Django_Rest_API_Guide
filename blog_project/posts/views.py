from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer
#from rest_framework import viewsets # new

# Using Normal Views
class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



# USING VIEWSETS
#class PostViewSet(viewsets.ModelViewSet): # new
    #permission_classes = (IsAuthorOrReadOnly,)
    #queryset = Post.objects.all()
    #serializer_class = PostSerializer


#class UserViewSet(viewsets.ModelViewSet): # new
    #queryset = get_user_model().objects.all()
    #serializer_class = UserSerializer
