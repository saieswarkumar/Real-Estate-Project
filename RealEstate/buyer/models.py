from django.db import models
from django.conf import settings
from seller.models import PropertyDetails

class PropertyRequests(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    requestedProperty = models.ForeignKey(PropertyDetails,on_delete=models.CASCADE)
    status = models.CharField(max_length=400,default='unsold')
    price = models.CharField(max_length=400)
    message = models.CharField(max_length=400)
