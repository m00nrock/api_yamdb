# Generated by Django 2.2.16 on 2022-02-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20220217_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('admin', 'user'), ('admin', 'moderator')], default='user', max_length=10),
        ),
    ]
