from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import parsers, renderers, status
from rest_framework.permissions import IsAuthenticated
from codeLabsApp.serializers import *
# Create your views here.
class RootView(APIView):
    def get(self, request):
        content = {'message': 'Hello, welcome to the task by Tiago Peres! Go to /api/users/ to test the post functionality'}
        return Response(content)

class MyUserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

""" 
JWT Auth. 
"""
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
