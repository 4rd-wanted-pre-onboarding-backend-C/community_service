from django.urls import path
from . import views
from .views import RegisterAPIView, DeleteUserView, SignInView

urlpatterns = [
    path("", views.accounts_app_home),
    path("register", RegisterAPIView.as_view()),
    path("delete/<int:pk>", DeleteUserView.as_view()),
    path("login", SignInView.as_view())
]