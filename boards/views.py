from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import FreePostSerializer,CommentSerializer,NoticePostSerializer, AdminPostSerializer
from .permissions import FreePostPermissions, CommentPermissions, AdminPostPermissions
from .models import FreePost, Comment, NoticePost, AdminPost


def board_app_home(request):
    return HttpResponse("Board app")


class AdminPostViewSet(ModelViewSet):
    """
    운영 게시판
    """
    queryset = AdminPost.objects.all()
    serializer_class = AdminPostSerializer
    permission_classes = [AdminPostPermissions]

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)
        return super().perform_create(serializer)


class FreePostViewSet(ModelViewSet):
    """
    자유 게시판, 댓글 기능 포함
    """
    queryset = FreePost.objects.all()
    serializer_class = FreePostSerializer
    permission_classes = [FreePostPermissions]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class CommentViewSet(ModelViewSet):
    """
    댓글 기능
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermissions]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class NoticePostViewSet(ModelViewSet):
    """
    공지 게시판
    """
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)
        return super().perform_create(serializer)
