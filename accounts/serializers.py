from rest_framework import serializers
from .models import TeamGroup,User


class TeamGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamGroup
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'