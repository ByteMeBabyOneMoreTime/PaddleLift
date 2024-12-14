from django.contrib import admin
from .models import job_listing, skill
# Register your models here.

admin.site.register(job_listing)
admin.site.register(skill)