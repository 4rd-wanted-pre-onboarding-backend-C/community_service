from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("admin-posts", views.JobPostViewSet)

urlpatterns = [
    path("", views.board_app_home),
    path("", include(router.urls))
]