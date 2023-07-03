from django.db import models
from django.utils import timezone
from shelters.models import Shelter


# Create your models here.
class Animal(models.Model):
    date_entered = models.DateTimeField(default=timezone.now)
    species = models.ForeignKey('Species', on_delete=models.SET_NULL, blank=False, null=True)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, blank=False, null=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, blank=False)
    views = models.IntegerField(default=0)
    availability = models.ForeignKey('Availability', on_delete=models.PROTECT)
    disposition = models.ManyToManyField('Disposition')
    size = models.ForeignKey('Size', on_delete=models.PROTECT)

    def __str__(self):
        return self.species + " " + self.age


class Species(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Availability(models.Model):
    availability = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.availability


class Disposition(models.Model):
    disposition = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.disposition

