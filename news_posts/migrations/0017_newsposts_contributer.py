# Generated by Django 3.2.8 on 2021-12-11 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0016_alter_newsposts_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsposts',
            name='contributer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
