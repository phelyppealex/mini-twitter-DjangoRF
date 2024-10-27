from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from follow_app.models import Follow
from api.serializers import FollowSerializer


class FollowListCreateAPIView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(following=user_profile)

class FollowRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)