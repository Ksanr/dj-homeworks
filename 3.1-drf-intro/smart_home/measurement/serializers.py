from rest_framework import serializers
from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы
class MeasurementSerializer(serializers.ModelSerializer):
    # Этот сериализатор используется для отображения отдельных записей измерений
    class Meta:
        model = Measurement
        fields = ['temperature', 'update_datetime', 'sensor', 'photo']



class SensorSerializer(serializers.ModelSerializer):
    # Используется для вывода краткого списка датчиков
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class SensorDetailSerializer(serializers.ModelSerializer):
    # Полная информация по датчику включает также связанные измерения
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']