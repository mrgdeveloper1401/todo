from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateMixin, UpdateMixixn, SoftDeleteMixin
from images.models import Images
from accounts.models import ProfileUser


class Workspace(CreateMixin, UpdateMixixn, SoftDeleteMixin):
    workspce_name = models.CharField(_("title workspace"), max_length=50)
    background_image = models.ForeignKey(Images, on_delete=models.PROTECT, related_name='workspace_image',
                              blank=True, null=True)
    workspace_description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(ProfileUser, related_name='workspace_members')
    is_active = models.BooleanField(default=True)
    
    class WorkspaceTypeChoices(models.TextChoices):
        education = 'ed', _('education')
        business = 'bs', _('business')
        engineer = 'eng', _('engineer')
        personal = 'pr', _('personal')
    workspce_type = models.CharField(max_length=3, choices=WorkspaceTypeChoices.choices)
    
        
    class Meta:
        db_table = 'workspace'
        verbose_name = _("worspace")
        verbose_name_plural = _("workspaces")
