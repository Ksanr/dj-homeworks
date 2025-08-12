from django.core.validators import slug_re
from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # В файле `models.py` нашего приложения создаём модель Phone с полями:
    # `id`, `name`, `price`, `image`, `release_date`, `lte_exists` и `slug`.
    # Поле `id` — должно быть основным ключом модели.
    # Значение поля `slug` должно устанавливаться слагифицированным значением поля `name`.
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=254, null=False)  # имя
    price = models.FloatField()  # цена
    image = models.CharField(max_length=254, null=False)  # ссылка на изображение
    release_date = models.DateField()  # дата релиза
    lte_exists = models.BooleanField()  # наличие lte
    slug = models.SlugField(unique=True) # слагирование из name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}, image: {self.image}, release_date: {self.release_date}, lte: {self.lte_exists}, slug: {self.slug}'
