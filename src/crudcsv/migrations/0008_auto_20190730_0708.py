# Generated by Django 2.1.1 on 2019-07-30 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudcsv', '0007_auto_20190729_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvupload',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
