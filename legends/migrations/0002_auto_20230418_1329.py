# Generated by Django 3.2.18 on 2023-04-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='slug',
            field=models.SlugField(default='slug', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='champion',
            name='title',
            field=models.CharField(default='champ name', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='champion',
            name='champion_name',
            field=models.CharField(default='champ', max_length=100, unique=True),
        ),
    ]
