from django.db import models
from solo.models import SingletonModel


class service(SingletonModel):
    class Meta:
        verbose_name = "1 - Range of Service"
    service1_heading = models.CharField(max_length=2500, default='')
    service1_video_url = models.URLField(max_length=255, default='')
    service2_heading = models.CharField(max_length=2500, default='')
    service2_video_url = models.URLField(max_length=255, default='')
    service3_heading = models.CharField(max_length=2500, default='')
    service3_video_url = models.URLField(max_length=255, default='')
    service4_heading = models.CharField(max_length=2500, default='')
    service4_video_url = models.URLField(max_length=255, default='')
    
    def __str__(self):
        return "Click to edit the Section"

class GlobalExpansion(SingletonModel):
    class Meta:
        verbose_name = "2 - Operations Around the World"
    
    description = models.CharField(max_length=4000)
    def __str__(self):
        return "Click to edit the Section"

class stats(SingletonModel):
    class Meta:
        verbose_name = "3 - Our Statistic"
    description = models.CharField(max_length=4000)
    ClientsServed = models.IntegerField()
    CandidatesPlaced = models.IntegerField()
    ClientRetentionRate = models.IntegerField()
    TurnAroundTime = models.IntegerField()
    JoiningRatio = models.IntegerField()
    CandidateSatisfactionRate = models.IntegerField()
    def __str__(self):
        return "Click to edit the Section"
    
    
class ClientsLogos(models.Model):
    class Meta:
        verbose_name = "4 - Our Client"
    
    name = models.CharField(max_length=2000)
    logo_url = models.URLField(max_length=255, default='')


class ClientsResponse(models.Model):
    class Meta:
        verbose_name = "5 - What Our Clients Say"
    image_url = models.URLField(max_length=255, default='')
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    response = models.TextField()

class about(SingletonModel):
    class Meta:
        verbose_name = "6 - About PaddleLift"
    
    description = models.CharField(max_length=4000)
    
    def __str__(self):
        return "Click to edit the Section"

class MissionAndVision(SingletonModel):
    class Meta:
        verbose_name = "7 - Our Vision, Mission & Core Values"
    
    vission_image_url = models.URLField(max_length=255, default="")
    vission_description = models.TextField()
    mission_image_url = models.URLField(max_length=255, default="")
    mission_description = models.TextField()
    
    def __str__(self):
        return "Click to edit the Section"