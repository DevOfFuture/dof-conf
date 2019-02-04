from django.db import models
from django.dispatch import receiver

from .models import Speaker


@receiver(models.signals.post_delete, sender=Speaker)
def auto_delete_photo_on_delete(sender, instance, **kwargs):
    if instance.photo:
        instance.photo.delete(False)


@receiver(models.signals.pre_save, sender=Speaker)
def auto_delete_photo_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_photo = sender.objects.get(pk=instance.pk).photo
    except sender.DoesNotExist:
        return False

    new_photo = instance.photo
    if not old_photo == new_photo:
        old_photo.delete(False)
