from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save)
def update_images(sender, instance, created, **kwargs):
    if created:
        pass