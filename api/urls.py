from django.urls import path
from mini_twitter_app.views import *

urlpatterns = [
    path('post/', PostListCreateAPIView.as_view(), name='post-create-list'),
    path('post/<int:pk>/', PostRetrieveDestroyAPIView.as_view(), name='post-detail-view'),

    path('person/', PersonCreateListView.as_view(), name='person-create-list'),
    path('person/<int:pk>/', PersonRetrieveDestroyAPIView.as_view(), name='person-detail-view'),
    
    path('like/', LikeListCreateAPIView.as_view(), name='like-create-list'),
    path('like/<int:pk>/', LikeRetrieveDestroyAPIView.as_view(), name='like-detail-view'),
]