from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    # serializers의 ModelSerializer 상속받음.
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')
        # fields = '__all__'
        # read_only_fields = ('title',)


