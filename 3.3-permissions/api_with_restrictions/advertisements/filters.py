import django_filters
from django.db.models import OuterRef, Exists
from django_filters import rest_framework as filters

from .models import Advertisement, FavouriteAdvertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lt')
    created_at_later = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    in_favourites = filters.BooleanFilter(method='filter_in_favourites')

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at_before', 'created_at_later', 'in_favourites']

    def filter_in_favourites(self, queryset, name, value):
        # Вариант 1. Попроще
        if self.request.user.is_authenticated:
            fav_query = FavouriteAdvertisement.objects.filter(user=self.request.user)
            queryset = queryset.filter(id__in=fav_query.values('advertisement'))
        elif value:
            queryset = queryset.none()
        return queryset

        # Вариант 2. Используя доп. возможности Django
        # if self.request.user.is_authenticated:
        #     favourite_subquery = FavouriteAdvertisement.objects.filter(advertisement_id=OuterRef('pk'), user=self.request.user).values_list('id')[:1]
        #     queryset = queryset.annotate(is_favoured=Exists(favourite_subquery)).filter(is_favoured=value)
        # elif value:
        #     queryset = queryset.none()
        # return queryset
