# Generated by Django 2.1.1 on 2019-07-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudcsv', '0003_auto_20190729_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvupload',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
