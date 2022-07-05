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
        verbose_name='Информация', blank=True, null=True
    )
    email = models.EmailField(
        verbose_name='Почта', max_length=254, unique=True
    )
    role = models.CharField(
        verbose_name='Роль', max_length=20, choices=ROLES, default=USER
    )
    confirmation_code = models.CharField(
        verbose_name='Код подтверждения', max_length=100,
        null=True, default=generate_confirmation_code()
    )

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.role == self.ADMIN:
            self.is_staff = True
        super().save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
