from rest_framework.serializers import ModelSerializer
from apps.posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'order']
        # fields = '__all__'