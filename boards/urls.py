from django.urls import include, path
from rest_framework import routers
from .views import FreePostViewSet,CommentViewSet

router = routers.DefaultRouter()
router.register('freepost', FreePostViewSet) # 자유게시판 게시글
router.register('comment', CommentViewSet) # 자유게시판 게시글의 댓글


app_name = 'board-api'

urlpatterns = [
    path('', include(router.urls)),
]
