import csv

from django.core.management.base import BaseCommand

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

FILES = {
    'users': User,
    'category': Category,
    'genre': Genre,
    'titles': Title,
    'review': Review,
    'comments': Comment,

}


class Command(BaseCommand):
    help = 'Импорт данных из .csv файла'

    def handle(self, *args, **options):
        for file, model in FILES.items():
            print(file)
            with open(
                f'static/data/{file}.csv',
                newline='',
                encoding='utf-8'
            ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row)
                    if 'author' in row:
                        row['author'] = User.objects.get(pk=row['author'])
                        print(row['author'])
                    if 'category' in row:
                        row['category'] = Category.objects.get(
                            pk=row['category'])
                        print(row['category'])
                    model.objects.create(**row)
