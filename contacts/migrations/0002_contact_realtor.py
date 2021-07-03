# Generated by Django 2.1.1 on 2019-07-24 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='realtor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor'),
            preserve_default=False,
        ),
    ]