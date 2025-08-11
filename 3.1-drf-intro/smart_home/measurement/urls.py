from django.urls import path
from measurement.views import SensorListCreate, SensorRetrieveUpdateDestroy, MeasurementCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorListCreate.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateDestroy.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]
