# Generated by Django 3.2.8 on 2021-10-13 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diarista',
            old_name='mumero',
            new_name='numero',
        ),
    ]