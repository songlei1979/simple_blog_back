from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models import Category, Post
from blog.permissions import IsAuthorOrReadOnly, isAuthor
from blog.serializers import CategorySerializer, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__name']
    permission_classes = [IsAuthorOrReadOnly]

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated and isAuthor(request):
            print(request.data)
            request.data._mutable = True
            request.data['author'] = request.user.id
            return super().create(request, *args, **kwargs)
        return Response("You have to be an author first", status=status.HTTP_403_FORBIDDEN)