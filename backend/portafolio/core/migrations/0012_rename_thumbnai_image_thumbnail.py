# Generated by Django 4.0.4 on 2023-11-09 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_title_album_name_rename_title_image_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='thumbnai',
            new_name='thumbnail',
        ),
    ]
