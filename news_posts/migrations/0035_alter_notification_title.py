# Generated by Django 3.2.8 on 2022-02-17 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0034_newsposts_saved_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
