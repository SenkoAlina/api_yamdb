import datetime
from django.core.exceptions import ValidationError


def validate_year(value):
    if value > datetime.datetime.today().year:
        raise ValidationError(
            'Год не может быть больше текущего',
            params={'value': value},
        )
