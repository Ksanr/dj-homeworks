# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from measurement.serializers import SensorListSerializer, SensorDetailSerializer, MeasurementSerializer
from measurement.models import Sensor, Measurement

# Список датчиков и создание нового датчика
class SensorListCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


# Детальная информация конкретного датчика + обновление/удаление
class SensorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Регистрация новой температуры для конкретного датчика
class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
"""
    def perform_create(self, serializer):
        sensor_id = self.request.data.get("sensor")
        try:
            sensor = Sensor.objects.get(id=sensor_id)
        except Sensor.DoesNotExist:
            return Response({"detail": "Датчик не найден."}, status=status.HTTP_404_NOT_FOUND)

        serializer.save(sensor=sensor)
"""