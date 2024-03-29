# Generated by Django 4.0.4 on 2024-01-04 12:22

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_home_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='cover',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='media/'),
        ),
    ]
