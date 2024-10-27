from rest_framework import serializers
from django.contrib.auth.models import User
from mini_twitter_app.models import Like, Post, Follow, UserProfile

class PostSerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['created', 'text_content', 'author', 'follower_count']
    
    def get_follower_count(self, obj):
        return obj.liked_count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    system_user = PublicUserSerializer(read_only=True)
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['username', 'name', 'created', 'system_user', 'follower_count', 'following_count']

    def get_follower_count(self, obj):
        return obj.follower_count()
    
    def get_following_count(self, obj):
        return obj.following_count()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        user_profile = UserProfile.objects.create(system_user=user, username=validated_data['username'], )
        user_profile.save()

        return user
