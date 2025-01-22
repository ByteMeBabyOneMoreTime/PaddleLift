from django.urls import path
from .views import *


urlpatterns = [
    path('get-service/', get_service_data, name='get_service_data'),
    path('operations-around-the-world/', global_expansion_view, name='global-expansion'),
    path('our-statistics/', stats_view, name='stats'),
    path('clients/', view=clients_logos_view, name='clients')
]
