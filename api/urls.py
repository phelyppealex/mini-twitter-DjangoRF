from django.urls import path
from post_app.views import *
from user_profile_app.views import *
from like_app.views import *
from follow_app.views import *

urlpatterns = [
    path('post/', PostListCreateAPIView.as_view(), name='post-create-list'),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail-view'),

    path('profile/', UserProfileCreateListView.as_view(), name='person-create-list'),
    path('profile/<str:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='person-detail-view'),
    
    path('like/', LikeListCreateAPIView.as_view(), name='like-create-list'),
    path('like/<int:pk>/', LikeRetrieveUpdateDestroyAPIView.as_view(), name='like-detail-view'),

    path('follow/', FollowListCreateAPIView.as_view(), name='follow-create-list'),
    path('follow/<int:pk>/', FollowRetrieveUpdateDestroyAPIView.as_view(), name='follow-detail-view'),

    path('feed/', UserFeedView.as_view(), name='user_feed')
]
