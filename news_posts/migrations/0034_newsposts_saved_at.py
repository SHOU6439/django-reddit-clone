# Generated by Django 3.2.8 on 2022-02-09 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_bookmarked_posts_created_at'),
        ('news_posts', '0033_auto_20220205_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsposts',
            name='saved_at',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_at', to='users.bookmarked_posts'),
        ),
    ]
