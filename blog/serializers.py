from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from blog.models import Category, Post


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content',
                  'updated_at', 'image', 'author', 'category', 'likes',
                  'category_name', 'author_username']
