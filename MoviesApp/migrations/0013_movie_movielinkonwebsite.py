# Generated by Django 4.2.1 on 2023-08-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0012_remove_movie_movielinkonwebsite'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movielinkonwebsite',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
