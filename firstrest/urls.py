from django.contrib import admin
from django.urls import path, include
from post import urls
from userpost import urls
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),     # url을 계층적으로 관리하기 위함
    path('userpost/', include('userpost.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# api서버 안에 로그인/로그아웃 버튼을 넣는 코드
