from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.http import request

from .models import Animal, Availability, Species


class AnimalListView(generic.ListView):
    model = Animal
    context_object_name = 'animals'


class AnimalDetailView(generic.DetailView):
    model = Animal
    context_object_name = 'animal'

    def get_animal(self):
        return Animal.objects.get(pk=self.kwargs.get("pk"))



