from django.db import models
from solo.models import SingletonModel


class service(SingletonModel):
    class Meta:
        verbose_name = "A - Range of Service"
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
        verbose_name = "B - Operations Around the World"
    
    description = models.CharField(max_length=4000)
    def __str__(self):
        return "Click to edit the Section"

class stats(SingletonModel):
    class Meta:
        verbose_name = "C - Our Statistic"
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
        verbose_name = "D - Our Client"
    
    name = models.CharField(max_length=2000)
    logo_url = models.URLField(max_length=255, default='')


class ClientsResponse(models.Model):
    class Meta:
        verbose_name = "E - What Our Clients Say"
    image_url = models.URLField(max_length=255, default='')
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    response = models.TextField()

class about(SingletonModel):
    class Meta:
        verbose_name = "F - About PaddleLift"
    
    description = models.CharField(max_length=4000)
    
    def __str__(self):
        return "Click to edit the Section"

class MissionAndVision(SingletonModel):
    class Meta:
        verbose_name = "G - Our Vision, Mission & Core Values"
    
    vission_image_url = models.URLField(max_length=255, default="")
    vission_description = models.TextField()
    mission_image_url = models.URLField(max_length=255, default="")
    mission_description = models.TextField()
    
    def __str__(self):
        return "Click to edit the Section"

class ManagementTeam(models.Model):
    class Meta: 
        verbose_name = "H - Meet the Management"

    name = models.CharField(max_length=400)
    position = models.CharField(max_length=400)
    role = models.CharField(max_length=400)
    linked_in_url = models.URLField(max_length=255)
    about_text = models.TextField()
    image_url = models.URLField(max_length=255)

class PersonalImages(models.Model):
    class Meta: 
        verbose_name = "I - Life at PaddleLift Images"

    image_url = models.URLField(max_length=255)

class OurServicesDescription(models.Model):
    class Meta: 
        verbose_name = "J - Our Services Description"

    description = models.TextField()

# -----
class IndustriesWeServeDescription(SingletonModel):
    class Meta:
        verbose_name = "K - Industries We Serve Description"
    
    description = models.TextField()

class IndustriesWeServeCards(models.Model):
    class Meta:
        verbose_name = "L - Industries We Serve Cards"

    name_of_industry = models.TextField()

class WhatSetsUsApartCards(SingletonModel):
    class Meta:
        verbose_name = "M - What Sets Us Apart Cards"
    
    card1_heading = models.CharField(max_length=500)
    card1_description = models.TextField()
    
    card2_heading = models.CharField(max_length=500)
    card2_description = models.TextField()
    
    card3_heading = models.CharField(max_length=500)
    card3_description = models.TextField()
    
    card4_heading = models.CharField(max_length=500)
    card4_description = models.TextField()
    
class OrganizationalStructureCards(SingletonModel):
    class Meta:
        verbose_name = "N - Organizational Structure Cards"
    
    card1_heading = models.CharField(max_length=500)
    card1_description = models.TextField()
    
    card2_heading = models.CharField(max_length=500)
    card2_description = models.TextField()
    
    card3_heading = models.CharField(max_length=500)
    card3_description = models.TextField()
    
    card4_heading = models.CharField(max_length=500)
    card4_description = models.TextField()

class OurPortfolioDescription(SingletonModel):
    class Meta:
        verbose_name = "O - Our Portfolio Description"
    
    description = models.TextField()

class FewSuccessStories(models.Model):
    class Meta:
        verbose_name = "P - Few Success Stories Cards"
    image_url = models.URLField(max_length=255, default='')
    heading = models.CharField(max_length=500)
    response = models.TextField()

class ContactInformation(SingletonModel):
    class Meta:
        verbose_name = "Q - Contact Information"
    
    call = models.CharField(max_length=400)
    WhatsApp = models.CharField(max_length=400)
    Email = models.EmailField(max_length=400)
    Address = models.TextField()

class Reviews(models.Model):
    class Meta:
        verbose_name = "R - Review"

    Username = models.CharField(max_length=400)
    rating = models.CharField(max_length=20)
    description = models.TextField()
    date = models.CharField(max_length=200)

    def __str__(self):
        return f"Name: {self.Username}, Rating: {self.rating}"