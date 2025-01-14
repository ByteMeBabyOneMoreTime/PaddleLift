from django.db.models.signals import pre_delete
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import *
from cloud.utils import *


@receiver(pre_delete, sender=ClientsLogos)
def before_delete_my_model3(sender, instance, **kwargs):
    try:
        id = get_file_id(instance.logo_url)
        delete_file(id)
    except:
        pass
