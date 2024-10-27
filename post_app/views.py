from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import render
from post_app.models import Post
from api.serializers import PostSerializerRequest
from mini_twitter_app.views import StandardPageNumberPagination

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerRequest
    pagination_class = StandardPageNumberPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerRequest
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user.profile:
            raise PermissionDenied("Você não pode editar esta publicação.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user.profile:
            raise PermissionDenied("Você não pode excluir esta publicação.")
        instance.delete()