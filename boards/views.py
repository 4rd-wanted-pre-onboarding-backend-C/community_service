from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from boards.serializers import AdminPostSerializer
from boards.models import AdminPost


def board_app_home(request):
    return HttpResponse("Board app")


class JobPostViewSet(ModelViewSet):
    queryset = AdminPost.objects.all()
    serializer_class = AdminPostSerializer
