# Generated by Django 3.2.8 on 2022-06-17 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0044_alter_vote_voted_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsposts',
            name='saved_at',
        ),
    ]
