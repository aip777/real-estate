# Generated by Django 2.1.1 on 2019-07-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20190630_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]