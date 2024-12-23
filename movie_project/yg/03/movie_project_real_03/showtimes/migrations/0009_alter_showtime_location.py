# Generated by Django 5.1.4 on 2024-12-23 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("showtimes", "0008_moviechain_rename_show_time_showtime_showtime_and_more"),
        ("single_pages", "0002_alter_showtime_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="showtime",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="showtimes_at_location",
                to="single_pages.movielocation",
            ),
        ),
    ]
