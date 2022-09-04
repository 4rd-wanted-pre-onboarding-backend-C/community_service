from rest_framework import serializers
from .models import FreePost,Comment

# 자유 게시판 댓글
class CommentSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Comment
        fields = ("pk", "post", "author", "content")


# 자유 게시판 글 목록 조회
class FreePostSerializer(serializers.ModelSerializer) :

    comments = CommentSerializer(many=True, read_only= True)
    # CommentSerializer를 포함하여 댓글 추가
    class Meta :
        model = FreePost
        fields = '__all__'


# 시리얼라이저의 목적은 유저가 입력한 데이터를 검증하고, Django 데이터로 변환하여 저장하게 하는 것
# 헤당 게시글에 대한 모든 정보를 역으로 json으로 변환하여 전달해야하는 시리얼 라이저와 차별화
# class FreePostCreateSerializer(serializers.ModelSerializer) :
#
#     class Meta :
#         model = FreePost
#         fields = ("title","content")