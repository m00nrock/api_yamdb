# Generated by Django 2.2.16 on 2022-02-16 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_category_comment_genre_review_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
