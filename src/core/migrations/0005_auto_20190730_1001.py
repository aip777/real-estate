# Generated by Django 2.1.1 on 2019-07-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190730_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, default=1, upload_to='books/pdfs/'),
            preserve_default=False,
        ),
    ]