# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response

from measurement.serializers import SensorListSerializer, SensorDetailSerializer, MeasurementSerializer
from measurement.models import Sensor, Measurement

# Список датчиков и создание нового датчика
class SensorList(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer
    # serializer_class = SensorDetailSerializer
    # def get_serializer_class(self):
    #
    #     if self.request.data.get("id"):
    #         serializer_class = SensorListSerializer
    #     else:
    #         serializer_class = SensorDetailSerializer


# Детальная информация конкретного датчика
class SensorDetailList(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Регистрация новой температуры для конкретного датчика
class Measurements(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def perform_create(self, serializer):
        sensor_id = self.request.data.get("sensor")
        try:
            sensor = Sensor.objects.get(id=sensor_id)
        except Sensor.DoesNotExist:
            return Response({"detail": "Датчик не найден."}, status=status.HTTP_404_NOT_FOUND)

        serializer.save(sensor=sensor)

