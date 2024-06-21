from django.db import models
from django.utils.translation import gettext_lazy as _
from todos.settings import AUTH_USER_MODEL
from core.models import CreateMixin, UpdateMixixn, CreateByMixin, SoftDeleteMixin
from accounts.models import ProfileUser
from django_jalali.db import models as jmodels
from workspaces.models import Workspace
from images.models import Images


class BackgorundColor(CreateMixin, UpdateMixixn):
    color = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.color
    
    class Meta:
        db_table = 'background_color'
        verbose_name = 'background_color'
        verbose_name_plural = 'background_colors'


class Board(CreateMixin, UpdateMixixn, SoftDeleteMixin):
    workspace = models.ForeignKey(Workspace, on_delete=models.PROTECT, related_name='workspace_boards')
    board_title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    background_image = models.ForeignKey(Images, on_delete=models.PROTECT, 
                        related_name='bg_image_board', blank=True, null=True)
    Backgorund_color = models.ForeignKey(BackgorundColor, on_delete=models.PROTECT,
                                         related_name='bg_color_board', blank=True, null=True)
    def __str__(self):
        return self.board_title

    class Meta:
        db_table = 'board'
        verbose_name = _('board')
        verbose_name_plural = _('boards')


class Card(CreateMixin, UpdateMixixn, SoftDeleteMixin):
    workspace = models.ForeignKey(Workspace, on_delete=models.PROTECT, related_name='workspace_card')
    board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name='board_card')
    card_title = models.CharField(max_length=100)
    card_body = models.TextField()
    expire_date = jmodels.jDateTimeField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.card_title} -- {self.card_body} -- {self.expire_date} -- {self.card_status}'

    class StatusCardChoices(models.TextChoices):
        doing = 'doing', _('doing')
        done = 'done', _('done')
        defined = 'defined', _('defined')
    card_status = models.CharField(max_length=7, choices=StatusCardChoices.choices)
    
    class Meta:
        db_table = 'card'
        verbose_name = _('card')
        verbose_name_plural = _('cards')


class ChatBoard(models.Model):
    workspace = models.OneToOneField(Workspace, on_delete=models.PROTECT, related_name='workpace_chat_board')
    board = models.OneToOneField(Board, on_delete=models.PROTECT, related_name='board_chat')
    user = models.ManyToManyField(ProfileUser, related_name='profile_chat')
    message = models.TextField()
    reply_to = models.ForeignKey('self', related_name='reply_chat', on_delete=models.PROTECT, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'chat_board'
        verbose_name = _('chat board')
        verbose_name_plural = _('chat boards')
