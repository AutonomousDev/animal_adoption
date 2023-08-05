"""
Rewriting the same file that lives in the animals app, because I do not know how to access it otherwise.
"""

from django_filters import (
    FilterSet,
    DateFromToRangeFilter,
    CharFilter,
    RangeFilter,
    MultipleChoiceFilter,
    ModelMultipleChoiceFilter,
)
from django.apps import apps


class AnimalFilter(FilterSet):
    date_entered = DateFromToRangeFilter()
    species = ModelMultipleChoiceFilter(
        queryset=apps.get_model("animals", "Species").objects.all()
    )
    breed = ModelMultipleChoiceFilter(
        queryset=apps.get_model("animals", "Breed").objects.all()
    )
    availability = ModelMultipleChoiceFilter(
        queryset=apps.get_model("animals", "Availability").objects.all()
    )
    disposition = ModelMultipleChoiceFilter(
        queryset=apps.get_model("animals", "Disposition").objects.all()
    )

    class Meta:
        model = apps.get_model("animals", "Animal")
        fields = [
            "name",
            "age",
            "size",
        ]