from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls, name="admin"),
    path('cron', include('cron.urls')),
    path('', home)
]
