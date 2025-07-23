from songBackend.models import Song

songs = [
    {'title': 'Song a', 'artist': 'Artist One', 'album': 'Album One', 'year': 2020, 'stream': 1000000},
    {'title': 'Song b', 'artist': 'Artist Two', 'album': 'Album Two', 'year': 2021, 'stream': 2000000},
    {'title': 'Song c', 'artist': 'Artist Three', 'album': 'Album Three', 'year': 2022, 'stream': 3000000},
    {'title': 'Song d', 'artist': 'Artist Four', 'album': 'Album Four', 'year': 2020, 'stream': 4000000},
    {'title': 'Song e', 'artist': 'Artist Five', 'album': 'Album Five', 'year': 2021, 'stream': 5000000},
    {'title': 'Song f', 'artist': 'Artist Six', 'album': 'Album Six', 'year': 2022, 'stream': 6000000},
    {'title': 'Song g', 'artist': 'Artist Seven', 'album': 'Album Seven', 'year': 2020, 'stream': 7000000},
    {'title': 'Song h', 'artist': 'Artist Eight', 'album': 'Album Eight', 'year': 2021, 'stream': 8000000},
    {'title': 'Song i', 'artist': 'Artist Nine', 'album': 'Album Nine', 'year': 2022, 'stream': 9000000},
    {'title': 'Song j', 'artist': 'Artist Ten', 'album': 'Album Ten', 'year': 2020, 'stream': 10000000},
    {'title': 'Song k', 'artist': 'Artist Eleven', 'album': 'Album Eleven', 'year': 2021, 'stream': 11000000},
    {'title': 'Song l', 'artist': 'Artist Twelve', 'album': 'Album Twelve', 'year': 2022, 'stream': 12000000},
    {'title': 'Song m', 'artist': 'Artist Thirteen', 'album': 'Album Thirteen', 'year': 2020, 'stream': 13000000},
]

for song_data in songs:
    Song.objects.create(**song_data)