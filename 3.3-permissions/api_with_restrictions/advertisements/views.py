from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .filters import AdvertisementFilter
from .models import Advertisement, FavouriteAdvertisement
from .permissions import IsOwnerOrAdminOrReadOnly
from .serializers import AdvertisementSerializer, FavouriteAdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
    filterset_class = AdvertisementFilter
    # filterset_fields = ['creator', 'created_at']
    ordering_fields = '__all__'


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdminOrReadOnly()]
        return []

    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user

        visible_statuses = ['OPEN', 'CLOSED']
        if not current_user.is_anonymous:
            visible_statuses.append('DRAFT')
        return queryset.filter(status__in=visible_statuses)


class FavouriteAdvertisementsViewSet(ModelViewSet):
    serializer_class = FavouriteAdvertisementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavouriteAdvertisement.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)