from django.contrib import admin
from .models import User, TeamGroup

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamGroup)
class TeamGroupAdmin(admin.ModelAdmin):
    pass