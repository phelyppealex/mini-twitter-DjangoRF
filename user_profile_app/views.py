from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from user_profile_app.models import UserProfile
from post_app.models import Post
from mini_twitter_app.views import StandardPageNumberPagination
from api.serializers import UserProfileSerializer, PostSerializerResponse

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