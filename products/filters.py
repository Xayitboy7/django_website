import django_filters
from .models import Glav, Roman

class GlavFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Glav
        model = Roman
        fields = ['name']