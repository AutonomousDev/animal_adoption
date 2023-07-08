from django.db import models
from django.contrib.auth.models import User
from shelters.models import Shelter


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employer = models.ForeignKey(Shelter, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
