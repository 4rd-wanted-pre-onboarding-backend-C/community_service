from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import FreePostSerializer,CommentSerializer
from .models import FreePost,Comment
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

def board_app_home(request):
    return HttpResponse("Board app")

class FreePostViewSet(viewsets.ModelViewSet):
    # authentication 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission 추가
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = FreePost.objects.all()
    serializer_class = FreePostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# 댓글 - Comment 보여주기, 수정하기, 삭제하기
class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # CommentSerializer에 있는 user 값을 채워주기 위해 perform_create 재정의
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

