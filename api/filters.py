"""
Rewriting the same file that lives in the animals app, because I do not know how to access it otherwise.
"""

from django_filters import (
    FilterSet,
    DateFromToRangeFilter,
    CharFilter,
    RangeFilter,
    MultipleChoiceFilter,
)
from django.apps import apps


class AnimalFilter(FilterSet):
    name = CharFilter(lookup_expr="contains")
    date_entered = DateFromToRangeFilter()
    age = RangeFilter()

    class Meta:
        model = apps.get_model("animals", "Animal")
        fields = [
            "name",
            "species",
            "age",
            "breed",
            "availability",
            "disposition",
            "size",
            "date_entered",
        ]
