from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    # 글 조회 권한 : 누구나 가능 / 글 생성 권한: 회원 / 글 편집 : 글 작성한 사람
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
