from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Advertisement, FavouriteAdvertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )
    is_favourite = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', 'is_favourite')

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user

        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        user = self.context['request'].user
        open_ads_count = Advertisement.objects.filter(creator=user, status='OPEN').count()

        if open_ads_count >= 10:
            raise serializers.ValidationError('Вы достигли лимита открытых объявлений.')

        return data

    def get_is_favourite(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return bool(obj.favourites.filter(user=user))

class FavouriteAdvertisementSerializer(serializers.ModelSerializer):
    """
    Serializer для избранных объявлений.
    """
    class Meta:
        model = FavouriteAdvertisement
        fields = '__all__'
        read_only_fields = ['user']  # Поле user устанавливается автоматически

    def validate(self, attrs):
        """
        Валидируем, что пользователь не добавляет свое собственное объявление в избранное.
        """
        request_user = self.context.get('request').user
        advertisement_creator = attrs['advertisement'].creator
        if request_user == advertisement_creator:
            raise serializers.ValidationError("Нельзя добавить своё объявление в избранное")
        return attrs