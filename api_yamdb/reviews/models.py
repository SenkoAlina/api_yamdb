from unicodedata import category
from django.db import models


class Category(models.Model):
    """Класс Category описывает модель для хранения информации о категориях"""

    name = models.CharField(
        verbose_name='Название',
        max_length=256
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Класс Genre описывает модель для хранения информации о жанрах"""

    name = models.CharField(
        verbose_name='Название',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    """Класс Title описывает модель для хранения информации о произведениях"""

    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        through='GenreTitle'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Класс GenreTitle описывает модель для хранения информации о связях между произведениями и жанрами"""

    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        verbose_name='Жанр',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title} {self.genre}'
