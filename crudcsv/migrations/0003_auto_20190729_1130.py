# Generated by Django 2.1.1 on 2019-07-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudcsv', '0002_auto_20190729_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvupload',
            name='images',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
