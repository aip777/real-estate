# Generated by Django 2.1.1 on 2019-06-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileband', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileband',
            name='email_address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profileband',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
