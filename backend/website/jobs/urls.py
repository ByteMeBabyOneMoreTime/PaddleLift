from django.urls import path

from .views import job_listings_json_view

urlpatterns = [
    path('jobs/', job_listings_json_view, name="Jobs"),
]