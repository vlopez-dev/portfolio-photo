# Generated by Django 4.2.7 on 2023-11-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_alter_home_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="coveralbum",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
