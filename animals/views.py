from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.http import request
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Animal, Shelter

class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    fields = [
        "name",
        "species",
        "age",
        "breed",
        "views",
        "availability",
        "disposition",
        "size"
    ]

    def get_context_data(self, *args, **kwargs):
        context = super(AnimalCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Add a new animal to your shelter"
        return context

    def form_valid(self, form):
        form.shelter = self.request.user.profile.shelter
        form.save()
        return super().form_valid(form)

class AnimalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Animal
    fields = [
        "name",
        "species",
        "age",
        "breed",
        "views",
        "availability",
        "disposition",
        "size"
    ]

    def test_func(self):
        """Check that the user is associated with the same shelter as the animal"""
        animal = self.get_object()
        if self.request.user.profile.shelter == animal.shelter:
            return True
        else:
            return False


class AnimalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Deletes the posts and redirects to home."""
    model = Animal
    success_url = '/'

    def test_func(self):
        """Check that the user is associated with the same shelter as the animal"""
        animal = self.get_object()
        if self.request.user.profile.shelter == animal.shelter:
            return True
        else:
            return False
    

class AnimalListView(generic.ListView):
    model = Animal
    context_object_name = 'animals'



class AnimalDetailView(generic.DetailView):
    model = Animal
    context_object_name = 'animal'

    def get_animal(self):
        return Animal.objects.get(pk=self.kwargs.get("pk"))
    




