# Generated by Django 4.2.1 on 2023-08-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0016_alter_movie_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='CompletedYESorNO',
            field=models.CharField(max_length=500, null=True),
        ),
    ]