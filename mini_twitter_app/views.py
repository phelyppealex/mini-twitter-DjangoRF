from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from mini_twitter_app.models import *
from api.serializers import *

class StandardPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# POST

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
    
# LIKE

class LikeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(person=self.request.user.profile)


class LikeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

# FOLLOW

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


# USER PROFILE

class UserProfileCreateListView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class UserProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserFeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializerResponse
    pagination_class = StandardPageNumberPagination

    def get_queryset(self):
        user_profile = self.request.user.profile
        following_profiles = user_profile.following_set.values_list('followed', flat=True)

        user_profile_id = user_profile.username

        profile_ids = list(following_profiles) + [user_profile_id]

        return Post.objects.filter(author__in=profile_ids).order_by('-created')

