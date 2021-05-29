from rest_framework import serializers
from api.models import Post,Author,Category,Comment
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author', 'profile_pic']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent','slug']
  

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ="__all__"
 
