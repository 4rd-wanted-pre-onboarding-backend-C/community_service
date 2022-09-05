from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import FreePostSerializer,CommentSerializer
from .permissions import CustomReadOnly
from .models import FreePost,Comment

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

