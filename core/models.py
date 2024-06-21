from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from todos.settings import AUTH_USER_MODEL
import jdatetime


class CreateMixin(models.Model):
    create_at = jmodels.jDateTimeField(_("create model"), auto_now_add=True)

    class Meta:
        abstract = True


class UpdateMixixn(models.Model):
    update_at = jmodels.jDateTimeField(_("update model"), auto_now=True)
    

    class Meta:
        abstract = True


class CreateByMixin(models.Model):
    create_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False, editable=False)
    deleted_at = jmodels.jDateTimeField(blank=True, null=True, editable=False)

    class Meta:
        abstract = True
