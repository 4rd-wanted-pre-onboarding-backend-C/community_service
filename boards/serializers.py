from rest_framework import serializers
from .models import AdminPost


class AdminPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminPost
        fields = "__all__"
