# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer
from .models import Sensor, Measurement

# Список датчиков и создание нового датчика
class CreateGetSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Детальная информация конкретного датчика
class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Регистрация новой температуры для конкретного датчика
class UpdateMeasurement(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer


