# Generated by Django 2.2.16 on 2022-07-02 20:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220703_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default=uuid.UUID('343b0232-fa44-11ec-a344-00d86116b68e'), max_length=100, null=True),
        ),
    ]
