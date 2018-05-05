# Generated by Django 2.0.4 on 2018-05-05 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180503_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='music.Album'),
        ),
        migrations.AlterField(
            model_name='track',
            name='artist',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='track',
            name='title',
            field=models.CharField(max_length=140),
        ),
    ]
