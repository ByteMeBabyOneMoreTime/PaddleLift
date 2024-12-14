from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('cron', include('cron.urls')),
    path('', home)
]
