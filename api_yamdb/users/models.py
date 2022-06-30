# import jwt

# from datetime import datetime, timedelta

# from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("User must have an username")
        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            username=username, email=self.normalize_email(email)
        )
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None, **extra_fields):

        if not username:
            raise ValueError("User must have an username")
        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            username=username, email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def create_moderator(self, username, email, password=None, **extra_fields):

        if not username:
            raise ValueError("User must have an username")
        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            username=username, email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = True

        return user


class User(AbstractBaseUser, PermissionsMixin):

    CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=150, choices=CHOICES, default='user')
    confirmation_code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    def __str__(self):
        return self.username
