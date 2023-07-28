from django import forms
from .models import Animal, Disposition


class AnimalCreateForm(forms.ModelForm):
    disposition = forms.ModelMultipleChoiceField(
        queryset=Disposition.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

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

class AnimalUpdateForm(AnimalCreateForm):
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
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            dispositions_all = Disposition.objects.all()
            self.fields['disposition'].queryset = dispositions_all
            self.fields['disposition'].initial = instance.disposition.all()