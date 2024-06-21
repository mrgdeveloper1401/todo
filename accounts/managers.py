from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManagers(BaseUserManager):
    def _create_user(self, email, mobile_phone, password=None, **extra_fields):
        if not email:
            raise ValueError('emil must be set')
        if not mobile_phone:
            raise ValueError('mobile phone must be set')
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            mobile_phone = mobile_phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, mobile_phone, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, mobile_phone=mobile_phone, password=password, **extra_fields)
    
    def create_superuser(self, email, mobile_phone, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email=email, mobile_phone=mobile_phone, password=password, **extra_fields)