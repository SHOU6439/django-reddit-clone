# Generated by Django 3.2.8 on 2022-02-22 04:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20220218_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='dminvite',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='invitation_room', to='chat.dmroom'),
            preserve_default=False,
        ),
    ]