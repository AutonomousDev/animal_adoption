from django.db import models
from .constants import (STATE_CHOICES)
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=100, null=False)

    addressLine1 = models.CharField(max_length=256, default='', blank=True)
    addressLine2 = models.CharField(max_length=256, default='', blank=True)
    addressLine3 = models.CharField(max_length=256, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='', blank=True)
    zip = models.CharField(max_length=5, default='', blank=True)

    phoneNumber = models.CharField(max_length=15, default='', blank=True)
    webSite = models.CharField(max_length=256, default='', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detailed record for this student"""
        return reverse('shelters-detail', args=[str(self.id)])
