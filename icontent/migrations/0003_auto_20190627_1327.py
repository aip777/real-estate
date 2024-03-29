# Generated by Django 2.1.1 on 2019-06-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icontent', '0002_auto_20190627_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='photo_1',
            new_name='photo_five',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='photo_2',
            new_name='photo_four',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='photo_3',
            new_name='photo_main_main',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='photo_4',
            new_name='photo_one',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='photo_5',
            new_name='photo_six',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='photo_6',
            new_name='photo_three',
        ),
        migrations.RemoveField(
            model_name='content',
            name='photo_main',
        ),
        migrations.AddField(
            model_name='content',
            name='bottom_details_one',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='bottom_details_three',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='bottom_details_two',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='photo_two',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='content',
            name='bottom_content_one',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='bottom_content_three',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='bottom_content_two',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='footer_facebook',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='footer_instragram',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='footer_linkedin',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='footer_pinterest',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='footer_twitter',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='header_email',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='content',
            name='header_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
