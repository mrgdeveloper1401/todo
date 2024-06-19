from django.contrib import admin
from boards.models import BackgorundColor, Board, Card, Tasks, Comment


@admin.register(BackgorundColor)
class BackgroundColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    pass
