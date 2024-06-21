from django.contrib import admin
from boards.models import BackgorundColor, Board, Card, ChatBoard


@admin.register(BackgorundColor)
class BackgroundColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(ChatBoard)
class ChatBoardAdmin(admin.ModelAdmin):
    pass
