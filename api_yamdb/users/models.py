# import string
# from random import random

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, **extra_fields):
        if username is None:
            raise TypeError('Обязательное поле')
        if email is None:
            raise TypeError('Обязательное поле')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def create_moderator(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Moderator must have is_staff=True.'))
        if extra_fields.get('is_superuser') is True:
            raise ValueError(_('Moderator cannot have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    CHOICES = (
        ('user', 'user'),
        ('moder', 'moderator'),
        ('admin', 'admin'),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=150, choices=CHOICES, default='user')

    objects = CustomUserManager()

    def str(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moder(self):
        return self.role == 'moder'

    @property
    def is_auth(self):
        return self.role == 'user'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
