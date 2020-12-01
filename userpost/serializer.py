from .models import UserPost
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    # author에 있는 username을 author_name으로 하겠다.
    class Meta:
        model = UserPost
        fields = ['pk', 'author_name', 'title', 'body']


