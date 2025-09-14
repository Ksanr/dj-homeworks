import django_filters
from django_filters import rest_framework as filters

from .models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lt')
    created_at_later = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')


    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at_before', 'created_at_later']
