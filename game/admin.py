from django.contrib import admin
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "winner", "is_finished", "duration")

    list_filter = ("is_finished", "winner")


    