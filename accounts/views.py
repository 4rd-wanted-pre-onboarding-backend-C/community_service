from django.http import HttpResponse
from rest_framework import viewsets,generics
from .serializers import TeamGroupSerializer,UserSerializer
from .models import TeamGroup,User



def accounts_app_home(request):
    return HttpResponse("Accounts app")

class TeamGroupViewSet(viewsets.ModelViewSet):
    queryset =  TeamGroup.objects.all()
    serializer_class = TeamGroupSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
