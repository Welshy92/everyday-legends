# Generated by Django 3.2.18 on 2023-04-26 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legends', '0004_alter_champion_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
    ]
