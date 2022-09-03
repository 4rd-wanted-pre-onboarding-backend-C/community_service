from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import NoticePostSerializer
from .models import NoticePost


def board_app_home(request):
    return HttpResponse("Board app")

class NoticePostViewSet(viewsets.ModelViewSet):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer