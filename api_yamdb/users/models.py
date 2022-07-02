from django.contrib.auth.models import AbstractUser
from django.db import models

from users.generate_code import generate_confirmation_code


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    ROLES = (
        (USER, 'user'),
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator')
    )

    bio = models.TextField(
        blank=True, null=True
    )
    email = models.EmailField(
        max_length=254, unique=True
    )
    password = models.CharField(
        'password', max_length=128, blank=True, null=True
    )
    role = models.CharField(
        max_length=20, choices=ROLES, default=USER
    )
    confirmation_code = models.CharField(
        max_length=100, null=True, default=generate_confirmation_code()
    )

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.role == self.ADMIN:
            self.is_staff = True
        super().save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
