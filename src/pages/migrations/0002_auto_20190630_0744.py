# Generated by Django 2.1.1 on 2019-06-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='video_url',
        ),
        migrations.AddField(
            model_name='gallery',
            name='video',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]