# Generated by Django 2.2.16 on 2022-07-02 20:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220703_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default=uuid.UUID('d2a2c7c6-fa46-11ec-a10b-70665589bd78'), max_length=100, null=True),
        ),
    ]