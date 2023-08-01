from django_filters import FilterSet, DateFromToRangeFilter, CharFilter, RangeFilter
from django_filters.widgets import RangeWidget
from .models import *


class AnimalFilter(FilterSet):
    name = CharFilter(lookup_expr="contains")
    date_entered = DateFromToRangeFilter(
        widget=RangeWidget(
            attrs={
                "type": "date"
            }
        )
    )
    age = RangeFilter(
        widget=RangeWidget(
            attrs={
                "type": "number",
                "min": 0
            }
        )
    )

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