from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.name
