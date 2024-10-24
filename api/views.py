from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mini_twitter_app.models import Person, Like, Post
from .serializers import PersonSerializer, LikeSerializer, PostSerializer

class PersonCreateListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)

# PERSON

@api_view(['GET'])
def getPersons(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addPerson(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# POST

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# LIKE

@api_view(['GET'])
def getLikes(request):
    likes = Like.objects.all()
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addLike(request):
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)