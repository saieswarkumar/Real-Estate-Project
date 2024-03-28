from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.urlresolvers import reverse
from general.choices import locusg
from general.models import Profile

class PropertyDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    ploatarea = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    balconies = models.IntegerField()
    totalrooms = models.IntegerField()
    totalfloors = models.IntegerField()
    houseimage = models.FileField()
    houseimage2 = models.FileField()
    houseimage3 = models.FileField()
    neighbour = models.CharField(max_length=400)
    aboutprop = models.CharField(max_length=400)
    cost = models.CharField(max_length=400,default='0')
    agents = models.IntegerField(default=0)
    status = models.CharField(max_length=100,default='unsold')

    def __unicode__(self):
        return self.name

class LocationDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    propid = models.ForeignKey(PropertyDetails,on_delete=models.CASCADE)
    locaddress = models.CharField(max_length=400)
    locationusage = models.CharField(max_length=4,choices=locusg)
    locationname = models.CharField(max_length=400)
    lati = models.FloatField(max_length=200)
    longi = models.FloatField(max_length=200)
    otherdetails = models.CharField(max_length=400)
    
    def __unicode__(self):
        return self.name