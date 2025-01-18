from django.urls import path
from .views import *


urlpatterns = [
    path('get-service/', get_service_data, name='get_service_data'),
    path('global-expansion/', global_expansion_view, name='global-expansion'),
]
