# Generated by Django 3.2.5 on 2021-07-15 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='public',
            field=models.BooleanField(default=False, verbose_name='public'),
        ),
    ]
