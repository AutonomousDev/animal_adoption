import django_filters
from .models import *


class AnimalFilter(django_filters.FilterSet):
    class Meta:
        model = Animal
        fields = [
            "name",
            "species",
            "age",
            "breed",
            "availability",
            "disposition",
            "size",
            "date_entered"
            ]
