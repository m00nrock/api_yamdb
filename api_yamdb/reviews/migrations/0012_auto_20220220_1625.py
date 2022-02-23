# Generated by Django 2.2.16 on 2022-02-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20220220_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.RenameField(
            model_name='review',
            old_name='score',
            new_name='rating',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_review'),
        ),
    ]
