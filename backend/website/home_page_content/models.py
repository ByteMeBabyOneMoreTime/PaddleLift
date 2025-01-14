from django.db import models
from solo.models import SingletonModel

class service(SingletonModel):
    class Meta:
        verbose_name = "1 - Serivice Names and Images"
    service1_heading = models.CharField(max_length=2500, default='')
    service1_image_url = models.URLField(max_length=255, default='')
    service2_heading = models.CharField(max_length=2500, default='')
    service2_image_url = models.URLField(max_length=255, default='')
    service3_heading = models.CharField(max_length=2500, default='')
    service3_image_url = models.URLField(max_length=255, default='')
    service4_heading = models.CharField(max_length=2500, default='')
    service4_image_url = models.URLField(max_length=255, default='')

class GlobalExpansion(SingletonModel):
    class Meta:
        verbose_name = "2 - Global Expansion Description"
    
    description = models.CharField(max_length=4000)

class OurStatisics(SingletonModel):
    class Meta:
        verbose_name = "3 - Our Statistics"

class ClientsLogos(models.Model):
    class Meta:
        verbose_name = "6 - Clients Logos"
    
    name = models.CharField(max_length=2000)
    logo_url = models.URLField(max_length=255, default='')
