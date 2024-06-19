from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _
from core.models import UpdateMixixn, CreateMixin


class  Users(AbstractBaseUser, PermissionsMixin, UpdateMixixn, CreateMixin):
    email = models.EmailField(unique=True)
    mobile_phone = models.CharField(max_length=15, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    
    USERNAME_FIELD = 'email'
    
    class Meta:
        db_table = 'users'
        verbose_name = _("user")
        verbose_name_plural = _("users")