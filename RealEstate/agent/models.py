from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.core.urlresolvers import reverse
from general.models import Profile

class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='user',on_delete=models.CASCADE)
    message = models.CharField(max_length=400)
    receiver = models.IntegerField()