from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from . import models


# Create your views here.
class ShelterDetailView(DetailView):
    model = models.Shelter


class ShelterListView(ListView):
    model = models.Shelter

