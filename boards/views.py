from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import NoticePostSerializer
from .models import NoticePost


def board_app_home(request):
    return HttpResponse("Board app")

class NoticePostViewSet(ModelViewSet):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)
        return super().perform_create(serializer)