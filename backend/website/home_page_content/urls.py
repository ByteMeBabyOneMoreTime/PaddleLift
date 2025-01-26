from django.urls import path
from .views import about_json_view, clients_logos_view, get_service_data, global_expansion_view, management_team_json_view, mission_and_vision_json_view, stats_view


urlpatterns = [
    path('get-service/', get_service_data, name='get_service_data'),
    path('operations-around-the-world/', global_expansion_view, name='global-expansion'),
    path('our-statistics/', stats_view, name='stats'),
    path('clients/', view=clients_logos_view, name='clients'),
    path('about/', about_json_view, name='about'),
    path('mission-and-vision/', mission_and_vision_json_view, name='mission_and_vision'),
    path('management/', management_team_json_view, name='management'),
]
