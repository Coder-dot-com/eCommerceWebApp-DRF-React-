from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

User = get_user_model()


@receiver(pre_save, sender=User, dispatch_uid="updateUser")
def updateUser(sender, instance, *args, **kwargs):
    user = instance
    if user.email != "":
        user.username = user.email
