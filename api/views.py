from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Posts
from .serializers import PostsSerializer

# Create your views here.
@api_view(['GET','DELETE','PUT'])
def get_delete_put_posts(request, pk):
    try:
        posts = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single post
    if request.method == 'GET':
        serializer = PostsSerializer(posts)
        return Response(serializer.data)
    
    #update details of a single post
    if request.method == 'PUT':
        serializer = PostsSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #delete a single post
    if request.method == 'DELETE':        
        serializer = PostsSerializer(posts)
        posts.delete()
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def get_post_posts(request):
    #get all Posts 
    if request.method == 'GET':
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    #Insert a new record for a posts
    if request.method == 'POST':
        data = {
            'title':request.data.get('title'),
            'author':request.data.get('author'),
            'content':request.data.get('content'),
        }
        serializer = PostsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)