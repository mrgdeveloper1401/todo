from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _
from core.models import UpdateMixixn, CreateMixin, SoftDeleteMixin
from django_jalali.db import models as jmodels
from accounts.managers import UserManagers


class  Users(AbstractBaseUser, PermissionsMixin, UpdateMixixn, CreateMixin):
    email = models.EmailField(unique=True)
    mobile_phone = models.CharField(max_length=15, unique=True)
    verify_email = models.BooleanField(default=False)
    verify_mobile_phone = models.BooleanField(default=False)
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
    REQUIRED_FIELDS = ('mobile_phone',)
    
    objects = UserManagers()
    
    class Meta:
        db_table = 'users'
        verbose_name = _("user")
        verbose_name_plural = _("users")
        

class ProfileUser(CreateMixin, UpdateMixixn, SoftDeleteMixin):
    user = models.OneToOneField(Users, on_delete=models.PROTECT, related_name='profile')
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birthday = jmodels.jDateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'profile_user'
        verbose_name = _('profile user')
        verbose_name_plural = _('profile users')