# Generated by Django 3.2.19 on 2023-06-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_music_app', '0004_alter_profile_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('pk',)},
        ),
        migrations.AlterField(
            model_name='album',
            name='image_URL',
            field=models.URLField(max_length=400),
        ),
    ]
