# Generated by Django 3.2.22 on 2023-11-01 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='image',
            new_name='imagehome',
        ),
    ]
