from rest_framework import serializers
from django.contrib.auth.models import User
from like_app.models import Like
from follow_app.models import Follow
from user_profile_app.models import UserProfile
from post_app.models import Post


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    following = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Follow
        fields = ['following', 'followed']

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

class PostSerializerResponse(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)
    follower_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['created', 'text_content', 'author', 'follower_count']
    
    def get_follower_count(self, obj):
        return obj.liked_count()
    
class PostSerializerRequest(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

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
