# Generated by Django 2.2.16 on 2022-02-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20220217_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user'), ('moderator', 'moderator')], default='user', max_length=10),
        ),
    ]
