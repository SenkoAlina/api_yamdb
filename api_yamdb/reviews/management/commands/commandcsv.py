import csv

from django.core.management.base import BaseCommand

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

FILES = {
    'users': User,
    'category': Category,
    'genre': Genre,
    'titles': Title,
    'genre_title': Title,
    'review': Review,
    'comments': Comment,
}


class Command(BaseCommand):
    help = 'Импорт данных из .csv файла'

    def handle(self, *args, **options):
        for file, model in FILES.items():
            with open(
                f'static/data/{file}.csv',
                newline='',
                encoding='utf-8'
            ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if file == 'genre_title':
                        genre = Genre.objects.get(pk=row['genre_id'])
                        title = model.objects.get(pk=row['title_id'])
                        title.genre.add(genre)
                        continue

                    if 'author' in row:
                        row['author'] = User.objects.get(pk=row['author'])
                    if 'category' in row:
                        row['category'] = Category.objects.get(
                            pk=row['category'])
                    model.objects.create(**row)
