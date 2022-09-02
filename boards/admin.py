from django.contrib import admin
from .models import AdminPost, FreePost, NoticePost, Comment


@admin.register(AdminPost)
class AdminPostAdmin(admin.ModelAdmin):
    pass


@admin.register(FreePost)
class FreePostAdmin(admin.ModelAdmin):
    pass


@admin.register(NoticePost)
class NoticePostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
