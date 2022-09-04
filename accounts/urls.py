from django.urls import path, include
from rest_framework import routers, urls
from . import views

# from .views import TeamGroupViewSet,UserViewSet

router = routers.DefaultRouter()
# router.register('accounts', UserViewSet)
# app_name = 'accounts-api'

urlpatterns = [
    # path('', include(router.urls)),
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),

]
