# Generated by Django 2.1.1 on 2019-06-30 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icontent', '0003_auto_20190627_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='photo_main_main',
            new_name='slider_photo_one',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='photo_one',
            new_name='slider_photo_three',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='photo_three',
            new_name='slider_photo_two',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='photo_two',
            new_name='slider_photos_main',
        ),
    ]
