# Generated by Django 3.2.8 on 2022-02-18 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_dmroom_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dmroom',
            name='users',
        ),
    ]
