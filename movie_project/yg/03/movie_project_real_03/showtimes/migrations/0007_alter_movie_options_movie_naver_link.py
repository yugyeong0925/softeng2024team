# Generated by Django 5.1.4 on 2024-12-23 05:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("showtimes", "0006_alter_movie_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="movie",
            options={"ordering": ["title"]},
        ),
        migrations.AddField(
            model_name="movie",
            name="naver_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
