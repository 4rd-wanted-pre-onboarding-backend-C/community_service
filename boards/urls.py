from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FreePostViewSet,CommentViewSet
from . import views

router = DefaultRouter()
router.register('freeposts', FreePostViewSet) # 자유게시판 게시글
router.register('comments', CommentViewSet) # 자유게시판 게시글의 댓글

app_name = 'board-api'

urlpatterns = router.urls + [
path("", views.board_app_home),
    path('', include(router.urls)),
]
