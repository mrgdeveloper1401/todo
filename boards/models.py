from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateMixin, UpdateMixixn, CreateByMixin
from todos.settings import AUTH_USER_MODEL
from django_jalali.db import models as jmodels
from workspaces.models import Workspace
from images.models import Images


class BackgorundColor(CreateMixin, UpdateMixixn, CreateByMixin):
    color = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'background_color'
        verbose_name = 'background_color'
        verbose_name_plural = 'background_colors'


class Board(CreateMixin, UpdateMixixn, CreateByMixin):
    workspace = models.ForeignKey(Workspace, on_delete=models.PROTECT, related_name='workspace_boards')
    board_title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    background_image = models.ForeignKey(Images, on_delete=models.PROTECT, 
                        related_name='bg_board', blank=True, null=True)
    Backgorund_color = models.ForeignKey(BackgorundColor, on_delete=models.PROTECT,
                                         related_name='bg_color_board')
        
    
    class Meta:
        db_table = 'board'
        verbose_name = _('board')
        verbose_name_plural = _('boards')


class Card(CreateMixin, UpdateMixixn, CreateByMixin):
    board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name='board_cards')
    title = models.CharField(max_length=100)
    seen = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'card'
        verbose_name = _('card')
        verbose_name_plural = _('cards')
        

class Tasks(CreateMixin, UpdateMixixn, CreateByMixin):
    card = models.ForeignKey(Card, on_delete=models.PROTECT, related_name='card_tasks')
    task_title = models.CharField(max_length=100)
    is_publish = models.BooleanField(default=True)
    Backgorund_color = models.ForeignKey(BackgorundColor, on_delete=models.PROTECT,
                                         related_name='bg_color_task')
    members = models.ManyToManyField(AUTH_USER_MODEL, related_name='task_members')
    validity_duration = jmodels.jDateTimeField()
    

class Comment(CreateMixin, UpdateMixixn, CreateByMixin):
    body_comment = models.TextField()
    is_publish = models.BooleanField(default=True)
    task = models.ForeignKey(Tasks, on_delete=models.PROTECT, related_name='task_comments')
    card = models.ForeignKey(Card, on_delete=models.PROTECT, related_name='card_comment')
    board = models.ForeignKey(Board, related_name='board_comments', on_delete=models.PROTECT)
    workspace = models.ForeignKey(Workspace, on_delete=models.PROTECT, related_name='worksapce_comments')
    reply_to = models.ForeignKey('self', on_delete=models.Prefetch, related_name='childreen')
        
    class Meta:
        db_table = 'comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
