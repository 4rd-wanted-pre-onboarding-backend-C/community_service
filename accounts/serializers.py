from rest_framework import serializers
from .models import TeamGroup, User
from django.contrib.auth.password_validation import validate_password # 패스워드의 기본 검증 도구
from rest_framework.authtoken.models import Token  #Token 모델
from rest_framework.validators import UniqueValidator  #이메일 중복 방지를 위한 검증 도구

class TeamGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamGroup
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

