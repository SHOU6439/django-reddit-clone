# Generated by Django 3.2.8 on 2022-06-10 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0011_alter_communities_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='communities',
            name='latest_posted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
