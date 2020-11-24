from django.contrib import admin
from django.urls import path, include
import post.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),     # url을 계층적으로 관리하기 위함

]
