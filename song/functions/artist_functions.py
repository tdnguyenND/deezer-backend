from song.models import Artist


def artist_from_name(name):
    qs = Artist.objects.filter(name__iexact=name)
    if qs.count() > 0:
        artist = qs.first()
    else:
        artist, created = Artist.objects.get_or_create(name=name)
    return artist
