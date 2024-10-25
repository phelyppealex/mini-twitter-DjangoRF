from rest_framework import generics
from mini_twitter_app.models import *
from api.serializers import *

# PERSON

class PersonCreateListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer = PersonSerializer(queryset, many=True)

class PersonRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer = PersonSerializer(queryset, many=True)

# POST

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)

class PostRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)

# LIKE

class LikeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer = LikeSerializer(queryset, many=True)

class LikeRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer = LikeSerializer(queryset, many=True)