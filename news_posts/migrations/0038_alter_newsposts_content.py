# Generated by Django 3.2.8 on 2022-02-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0037_alter_newsposts_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsposts',
            name='content',
            field=models.CharField(blank=True, max_length=524, null=True),
        ),
    ]
