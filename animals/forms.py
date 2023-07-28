from django import forms
from .models import Animal


class AnimalCreateForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "name",
            "species",
            "age",
            "breed",
            "disposition",
            "size",
            "image"
        ]
        widgets = {
            'age': forms.NumberInput(attrs={'min': 0}),
        }