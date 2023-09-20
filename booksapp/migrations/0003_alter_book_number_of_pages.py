# Generated by Django 4.2.5 on 2023-09-20 08:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0002_author_language_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2)]),
        ),
    ]