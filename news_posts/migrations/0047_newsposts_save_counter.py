# Generated by Django 3.2.8 on 2022-06-22 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0046_auto_20220617_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsposts',
            name='save_counter',
            field=models.IntegerField(default=0),
        ),
    ]