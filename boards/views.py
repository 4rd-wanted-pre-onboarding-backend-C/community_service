from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import FreePostSerializer,CommentSerializer,NoticePostSerializer
from .permissions import CustomReadOnly
from .models import FreePost,Comment,NoticePost


def board_app_home(request):
    return HttpResponse("Board app")

class FreePostViewSet(viewsets.ModelViewSet):

    queryset = FreePost.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return FreePostSerializer
        return FreePostSerializer
    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)
        return super().perform_create(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return CommentSerializer

class NoticePostViewSet(ModelViewSet):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)
        return super().perform_create(serializer)
