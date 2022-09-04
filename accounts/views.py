from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.serializers import RegisterSerializer


def accounts_app_home(request):
    return HttpResponse("Accounts app")


class RegisterAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeleteUserView(DestroyAPIView):
    queryset = get_user_model().objects.all()
