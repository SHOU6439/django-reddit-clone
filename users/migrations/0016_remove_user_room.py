# Generated by Django 3.2.8 on 2022-02-18 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_user_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='room',
        ),
    ]
