# Generated by Django 3.2.8 on 2022-06-01 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0041_newsposts_latest_commented_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='latest_replayed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
