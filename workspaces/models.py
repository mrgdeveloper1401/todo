from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateMixin, UpdateMixixn
from images.models import Images


class Workspace(CreateMixin, UpdateMixixn):
    workspce_name = models.CharField(_("title workspace"), max_length=50)
    background_image = models.ForeignKey(Images, on_delete=models.PROTECT, related_name='workspace_image',
                              blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'workspace'
        verbose_name = _("worspace")
        verbose_name_plural = _("workspaces")
