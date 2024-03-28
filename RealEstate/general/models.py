from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.urlresolvers import reverse
from .choices import *

class Profile(AbstractUser):
    location = models.CharField(max_length=30, blank=True)
    user_type = models.CharField(max_length=2,
                                 choices=type_choices)
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()