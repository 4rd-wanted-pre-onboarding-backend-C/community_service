from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from boards.views import NoticePostViewSet, board_app_home

router = routers.DefaultRouter()
router.register('noticeposts',NoticePostViewSet)

urlpatterns = [
    path('board_app_home/', board_app_home),
    path('adimn/',admin.site.urls),
    path('',include(router.urls))
]