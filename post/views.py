from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer

# CBV


class PostViewSet(viewsets.ModelViewSet):
    # PostViewSet이 CRUD를 담당하는 클래스
    queryset = Post.objects.all()
    serializer_class = PostSerializer

