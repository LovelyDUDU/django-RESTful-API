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
########################################################################
'''
# APIView를 이용 (CBV class based View 방식으로 구현됨)

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
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)  # 쿼리셋 넘기기 (many=True 인자)
        return Response(serializer.data)    # 직접 Response 리턴해지구 : serializer.data

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):

    def get_object(self, pk):
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
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

########################################################################
# # 여기서 부터는 mixin 내용
# # 불필요한 것을 줄이자 -> mixins ==> 상속을 하자.
# # queryset과 serializer_class는 GenericAPIView의 변수
# # *args와 **kwargs 는 가변인자 => 받은 인자의 개수에 무관한 인자
# # *args = non keyword argument : 키워드가 아닌 인자를 받아줌
# # **kwargs = 키워드인 인자를 받아줌
# # APIView로는 일일이 중복되는 코드가 많고 귀찮아서 상속의 개념을 사용해서 줄임
#
# # 데이터 처리 대상 : 모델, Serializer import 시키기
#
# from post.models import Post
# from post.serializer import PostSerializer
# from rest_framework import generics
# from rest_framework import mixins
#
#
# class PostList(mixins.ListModelMixin, mixins.CreateModelMixin,
#                generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     # get은 list를 내보내는 메소드
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     # post는 create를 내보내는 메소드
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PostDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
#                  mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     # DetailView의 get은 retrieve를 내보내는 메소드
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

########################################################################

# # generic CBV
# from post.models import Post
# from post.serializer import PostSerializer
# from rest_framework import generics
#
#
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

########################################################################
# viewset 이용 -> urls.py에서 router 사용함

from post.models import Post
from post.serializer import PostSerializer

from rest_framework import viewsets

# @action처리
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

# ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능

# ReadOnlyModelViewSet 는 GET(조회) 만 가능함
# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # @action(method=['post'])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 customapi
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")