from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import *
from .utils import *

@receiver(pre_delete, sender=CV)
def before_delete_my_model(sender, instance, **kwargs):
    try:
        id = get_file_id(instance.cv_url)
        print(id)
        delete_file(id)
    except:
        pass