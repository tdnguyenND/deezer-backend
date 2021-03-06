# Generated by Django 3.1.7 on 2021-03-22 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0003_song_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'artist',
            },
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.CreateModel(
            name='SongArtist',
            fields=[
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.artist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.song')),
            ],
            options={
                'db_table': 'song_artist',
            },
        ),
    ]
