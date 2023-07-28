from django.db import models
from django.contrib.auth.models import User
from shelters.models import Shelter


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    shelter = models.OneToOneField(Shelter, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def is_shelter(self):
        if self.shelter is None:
            return False
        else:
            return True
