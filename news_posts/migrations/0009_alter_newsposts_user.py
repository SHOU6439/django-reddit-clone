# Generated by Django 3.2.8 on 2021-11-29 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_username'),
        ('news_posts', '0008_alter_newsposts_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsposts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
