from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import ClientsLogos, ClientsResponse, ManagementTeam, MissionAndVision
from cloud.utils import get_file_id, delete_file


@receiver(pre_delete, sender=ClientsLogos)
def before_delete_my_model3(sender, instance, **kwargs):
    try:
        id = get_file_id(instance.logo_url)
        delete_file(id)
    except Exception as e:
        print(f"{e}")

@receiver(pre_delete, sender=ClientsResponse)
def before_delete_my_clientsResponse(sender, instance, **kwargs):
    try:
        id = get_file_id(instance.image_url)
        delete_file(id)
    except Exception as e:
        print(f"{e}")

@receiver(pre_delete, sender=MissionAndVision)
def before_delete_my_MissionAndVision(sender, instance, **kwargs):
    try:
        id = get_file_id(instance.vission_image_url)
        delete_file(id)
        id = get_file_id(instance.mission_image_url)
        delete_file(id)
    
    except Exception as e:
        print(f"{e}")

@receiver(pre_delete, sender=ManagementTeam)
def before_delete_my_ManagementTeam(sender, instance, **kwargs):
    try:
        id = get_file_id(instance.image_url)
        delete_file(id)
    except Exception as e:
        print(f"{e}")