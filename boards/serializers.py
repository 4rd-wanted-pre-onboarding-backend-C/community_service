from rest_framework import serializers
from .models import NoticePost

class NoticePostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d T%H:%M:%S", "%Y-%m-%d"],
                                           read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d T%H:%M:%S", "%Y-%m-%d"],
                                           read_only=True)
    author_username = serializers.SlugRelatedField(read_only=True, slug_field='username', source="author")


    class Meta:
        model = NoticePost
        fields = ["id",
                "created_at",
                "updated_at",
                "title",
                "content",
                "is_fixed",
                "author_username"]