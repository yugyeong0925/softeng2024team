# Generated by Django 5.1.4 on 2024-12-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("showtimes", "0002_remove_movie_movie_chain_alter_movie_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="showtime",
            name="duration",
        ),
        migrations.AddField(
            model_name="movie",
            name="duration",
            field=models.IntegerField(blank=True, default=120, null=True),
        ),
    ]