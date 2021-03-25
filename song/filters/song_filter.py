from song.models import Song
from django_filters import FilterSet, CharFilter

class SongFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    artist = CharFilter(field_name='songartist__artist__name', lookup_expr='icontains')
    owner = CharFilter(field_name='owner__name', lookup_expr='icontains')

    class Meta:
        model = Song
        fields = ['title']