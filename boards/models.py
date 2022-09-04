from django.db import models
from django.contrib.auth import get_user_model


class TimeStampedModel(models.Model):
    """
    created_at, updated_at 필드 생성을 위한 기본 모델
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CommonPostModel(models.Model):
    """
    모든 게시물이 공유하는 필드 생성을 위한 기본 모델
    """
    title = models.CharField(max_length=40)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True


class FreePost(TimeStampedModel, CommonPostModel):
    """
    자유 게시판 게시물 모델, 댓글 기능 추가
    """

    def __str__(self):
        return f'<Free Post - {self.title}>'


class NoticePost(TimeStampedModel, CommonPostModel):
    """
    공지 게시판 게시물 모델, 고정 게시물 기능 추가
    """
    is_fixed = models.BooleanField(default=False)

    def __str__(self):
        return f'<Notice Post - {self.title}>'


class AdminPost(TimeStampedModel, CommonPostModel):
    """
    운영자 게시판 게시물 모델, 헤드 이미지 기능 추가
    """
    head_image = models.ImageField(blank=True, upload_to="admin_post_image/%Y/%m/%d")

    def __str__(self):
        return f'<Admin Post - {self.title}>'


class Comment(TimeStampedModel):
    """
    자유 게시판의 게시물에 달리는 댓글 모델
    """
    post = models.ForeignKey('FreePost', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f'<Comment - {self.content}>'
