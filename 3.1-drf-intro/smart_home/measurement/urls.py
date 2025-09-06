from rest_framework import routers
from django.urls import path, include
from .views import CreateGetSensorView, SensorView, UpdateMeasurement

# router = routers.DefaultRouter()
# router.register(r'sensors', SensorList)
# router.register(r'measurements', Measurements)

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path(r'sensors/', CreateGetSensorView.as_view()),
    path(r'sensors/<pk>/', SensorView.as_view()),
    path(r'measurements/', UpdateMeasurement.as_view()),
]
