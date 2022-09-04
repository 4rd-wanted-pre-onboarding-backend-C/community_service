from django.urls import path
from . import views
from .views import RegisterAPIView

urlpatterns = [
    path("", views.accounts_app_home),
    path("register", RegisterAPIView.as_view()),
]