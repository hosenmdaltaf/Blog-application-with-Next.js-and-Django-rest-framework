from django.shortcuts import render
from django.contrib.auth.models import User
from api.serializers import PostSerializer
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from api.models import Post,Category,Author

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# class PostList(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()



class PostList(generics.ListAPIView):
   serializer_class = PostSerializer
   queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):
   serializer_class = PostSerializer
   queryset = Post.objects.all()





# class PostDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404




# class PostLCSerializer(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
   

# class PostRUDSerializer(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

 
