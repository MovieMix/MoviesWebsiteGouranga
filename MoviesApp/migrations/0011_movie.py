# Generated by Django 4.2.1 on 2023-08-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0010_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('released', models.DateField()),
                ('desc', models.CharField(max_length=500)),
                ('genre1', models.CharField(max_length=500)),
                ('genre2', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
                ('downloadlDIRECTlink', models.CharField(max_length=500)),
                ('watchmovielink', models.CharField(max_length=500)),
                ('movielinkonwebsite', models.CharField(max_length=500)),
                ('imdb', models.FloatField()),
                ('image_file', models.FileField(upload_to='')),
            ],
        ),
    ]
