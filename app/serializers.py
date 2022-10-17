from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from app.models import Post


class PostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ('created_at', 'updated_at')

# and here
