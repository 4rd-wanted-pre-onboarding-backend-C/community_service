from django.contrib import admin
from .models import User, TeamGroup, History

# Register your models here.

@admin.register(User)
class AdminPostAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamGroup)
class FreePostAdmin(admin.ModelAdmin):
    pass


@admin.register(History)
class NoticePostAdmin(admin.ModelAdmin):
    pass