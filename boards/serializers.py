from dataclasses import field
from rest_framework import serializers
from .models import NoticePost

class NoticePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticePost
        fields = ('author','title','content','is_fixed')