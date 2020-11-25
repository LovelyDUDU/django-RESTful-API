'''
# viewsets 를 이용
from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer

# CBV


class PostViewSet(viewsets.ModelViewSet):
    # PostViewSet이 CRUD를 담당하는 클래스
    queryset = Post.objects.all()
    serializer_class = PostSerializer

'''

# APIView를 이용
# 데이터 처리 대상
from post.models import Post
from post.serializer import PostSerializer

# staus에 따라 직접 Response를 처리할 것
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# APIView를 상속받은 CBV
from rest_framework.views import APIView

# PostDetail 클래스의 get_object 메소드 대신 이거 써도 된다.
# from django.shortcuts import get_object_or_404

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)  # 쿼리셋 넘기기 (many=True 인자)
        return Response(serializer.data)    # 직접 Response 리턴해지구 : serializer.data

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDeatil(APIView):

    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()