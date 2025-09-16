from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
    DRAFT = "DRAFT", "Черновик"


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.DRAFT
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class FavouriteAdvertisement(models.Model):
    """
    Модель избранных объявлений. Связывает пользователя и объявление.
    """
    advertisement = models.ForeignKey(Advertisement, related_name="favourites", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="favourite_ads", on_delete=models.CASCADE)

    class Meta:
        unique_together = ['advertisement', 'user']

    def __str__(self):
        return f"{self.user.username}'s favourite ad {self.advertisement.title}"