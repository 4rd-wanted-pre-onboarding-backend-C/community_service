from rest_framework import serializers
from .models import FreePost, Comment, NoticePost
from .models import AdminPost


class AdminPostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d T%H:%M:%S", "%Y-%m-%d"],
                                           read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d T%H:%M:%S", "%Y-%m-%d"],
                                           read_only=True)
    author_username = serializers.SlugRelatedField(read_only=True, slug_field='username', source="author")
    head_image_url = serializers.SerializerMethodField()
    head_image_file = serializers.ImageField(source='head_image', write_only=True, allow_null=True)

    class Meta:
        model = AdminPost
        fields = ["id",
                  "created_at",
                  "updated_at",
                  "title",
                  "content",
                  "head_image_url",
                  "head_image_file",
                  "author_username"]

    def get_head_image_url(self, obj):
        return obj.head_image.url if obj.head_image else "게시물에 첨부된 헤드 이미지가 없습니다."


# 자유 게시판 댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("pk", "post", "author", "content")


# 자유 게시판 글 목록 조회
class FreePostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author_username = serializers.SlugRelatedField(read_only=True, slug_field='username', source="author")

    # CommentSerializer를 포함하여 댓글 추가
    class Meta:
        model = FreePost
        fields = ["id",
                  "created_at",
                  "updated_at",
                  "title",
                  "content",
                  "author_username",
                  "comments",
                  ]


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
