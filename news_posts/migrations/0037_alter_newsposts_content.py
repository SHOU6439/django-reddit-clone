# Generated by Django 3.2.8 on 2022-02-17 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0036_alter_notification_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsposts',
            name='content',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
