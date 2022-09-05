from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import FreePostViewSet,CommentViewSet,NoticePostViewSet, AdminPostViewSet, board_app_home

router = DefaultRouter()
router.register('freeposts', FreePostViewSet) # 자유게시판 게시글
router.register('comments', CommentViewSet) # 자유게시판 게시글의 댓글
router.register('noticeposts',NoticePostViewSet)
router.register("admin-posts", AdminPostViewSet)

urlpatterns = [
    path('board_app_home/', board_app_home),
    path('',include(router.urls)),
]
