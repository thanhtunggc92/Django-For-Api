from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from .models import Post
from .serializer import TaskSerializer

@api_view(['GET'])
def PostListView(request):
    model= Post.objects.all()
    serializer= TaskSerializer(model, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PostDetail(request,pk):
    permission_classes= (permissions.IsAuthenticatedOrReadOnly)
    post_id= Post.objects.get(id=pk)
    serializer= TaskSerializer(post_id, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def PostCreate(request):

    serializer= TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def PostUpdate(request,pk):
    post_id=Post.objects.get(id=pk)
    serializer= TaskSerializer(instance=post_id,  data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def PostDelete(request,pk):
    post_id=Post.objects.get(id=pk)
    post_id.delete()
    return Response('You are successfully delete the item')
