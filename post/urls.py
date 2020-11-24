from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# django rest framework는 router라는 것을 통해서 url을 결정한다.

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
