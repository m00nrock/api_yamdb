# Generated by Django 2.2.16 on 2022-02-20 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_auto_20220220_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='score',
        ),
    ]
