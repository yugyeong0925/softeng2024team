# Generated by Django 5.1.4 on 2024-12-23 05:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("showtimes", "0004_rename_showtime_showtime_show_time_alter_movie_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="movie_images/"),
        ),
    ]
