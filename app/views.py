from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from app.models import Post
from app.serializers import PostModelSerializer


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    lookup_url_kwarg = 'id'
    serializer_class = PostModelSerializer
    parser_classes = [MultiPartParser]

