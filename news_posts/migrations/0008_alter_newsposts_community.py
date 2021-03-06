# Generated by Django 3.2.8 on 2021-11-24 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_communities_updated_at'),
        ('news_posts', '0007_newsposts_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsposts',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community', to='communities.communities'),
        ),
    ]
