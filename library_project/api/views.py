import imp
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from books.models import Book
from .serializers import ItemSerializers
# Create your views here.


@api_view(['GET'])
def BookAPIView(request):
    book=Book.objects.all()
    serializer= ItemSerializers(book,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def AddBookItem(request):
    serializer=ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
