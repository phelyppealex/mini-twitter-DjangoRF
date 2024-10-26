from rest_framework import serializers
from mini_twitter_app.models import Person, Like, Post, Follow

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # def create(self, validated_data):
    #     # Extraindo o username do author
    #     author_username = validated_data.pop('author', None)
    #     author = None
        
    #     if author_username:
    #         try:
    #             author = Person.objects.get(username=author_username)
    #         except Person.DoesNotExist:
    #             raise serializers.ValidationError("Author does not exist.")
        
    #     validated_data['author'] = author
    #     return super().create(validated_data)

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'
