'''
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# django rest framework는 router라는 것을 통해서 url을 결정한다.

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
'''

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Default Router 사용 x --> API ROOT 없음

urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDeatil.as_view())
]