from django.urls import path
from .views import get_service_data

urlpatterns = [
    path('get-service/', get_service_data, name='get_service_data'),
]
