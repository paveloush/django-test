# Generated by Django 2.0.4 on 2018-05-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.SmallIntegerField(verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DurationField(verbose_name='Продолжительность'),
        ),
    ]
