# Generated by Django 2.0.4 on 2018-05-03 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Название')),
                ('year', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=140, verbose_name='Исполнитель')),
                ('title', models.CharField(max_length=140, verbose_name='Название')),
                ('duration', models.DurationField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album', verbose_name='Альбом')),
            ],
        ),
    ]