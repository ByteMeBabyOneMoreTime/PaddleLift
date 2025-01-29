from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Review_scheduling

@admin.register(Review_scheduling)
class Review(ModelAdmin):
    pass
