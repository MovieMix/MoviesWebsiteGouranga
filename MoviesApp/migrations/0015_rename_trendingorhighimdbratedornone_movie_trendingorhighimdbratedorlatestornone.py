# Generated by Django 4.2.1 on 2023-08-12 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0014_movie_trendingorhighimdbratedornone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='trendingORHighImdbratedORNone',
            new_name='trendingORHighImdbratedORLatestORNone',
        ),
    ]
