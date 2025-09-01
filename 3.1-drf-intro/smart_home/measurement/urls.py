from rest_framework import routers
from django.urls import path, include
from measurement.views import SensorList, Measurements, SensorDetailList

router = routers.DefaultRouter()
router.register(r'sensors', SensorList)
router.register(r'measurements', Measurements)

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path(r'sensors/<pk: int>/', SensorDetailList.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
