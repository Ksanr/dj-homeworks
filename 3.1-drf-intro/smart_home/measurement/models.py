from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.id}: {self.name}'

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Температура')
    update_datetime = models.DateTimeField(verbose_name='Дата и время измерения', auto_now=True)
    photo = models.ImageField(verbose_name='Фото', null=True, blank=True)

    def __str__(self):
        return f'Температура {self.temperature}°C в {self.sensor.name}'
