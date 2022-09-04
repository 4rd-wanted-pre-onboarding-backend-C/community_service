from django.urls import include, path
from rest_framework import routers
from .views import FreePostViewSet,CommentViewSet

router = routers.SimpleRouter()
router.register('freeposts', FreePostViewSet) # 자유게시판 게시글
router.register('comments', CommentViewSet) # 자유게시판 게시글의 댓글

app_name = 'board-api'

urlpatterns = router.urls + [
    path('', include(router.urls)),
]
