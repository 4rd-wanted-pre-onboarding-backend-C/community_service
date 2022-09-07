from rest_framework import permissions


class FreePostPermissions(permissions.BasePermission):
    """
    로그인하지 않은 사람은 조회만 가능, 로그인해야지만 생성, 수정, 삭제
    """

    def has_object_permission(self, request, view, obj):
        """
        모두 : SAFE_METHODS (GET,HEAD, OPTIONS) 요청 가능
        로그인 한 유저 : POST 요청만 보낼 수 있음
        로그인 했고, 글의 저자만 : PUT, DELETE 요청을 보낼 수 있음
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == "POST":
            return request.user.is_authenticated
        else:
            return obj.author == request.user


class CommentPermissions(FreePostPermissions):
    """
    FreePostPermissions 와 동일
    """
    pass


class AdminPostPermissions(permissions.BasePermission):
    """
    운영 게시판 - is_staff, is_superuser 권한을 가진 사람만 CRUD 가 가능
    """

    def has_object_permission(self, request, view, obj):
        """
        현재 유저가 스태프 권한을 가지고 있고, 슈퍼 유저라면 모든 권한을 부여
        """
        return request.user.is_staff and request.user.is_superuser

