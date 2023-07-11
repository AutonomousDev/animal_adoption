from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Shelter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class ShelterDetailView(DetailView):
    model = Shelter


class ShelterListView(ListView):
    model = Shelter


class ShelterCreateView(LoginRequiredMixin, CreateView):
    model = Shelter
    fields = [
        "name",
        "addressLine1",
        "addressLine2",
        "addressLine3",
        "city",
        "state",
        "zip",
        "phoneNumber",
        "webSite",
    ]

    def get_context_data(self, *args, **kwargs):
        context = super(ShelterCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create Job"
        return context

    def form_valid(self, form):
        new_shelter = form.save()
        user_profile = self.request.user.profile
        user_profile.shelter = new_shelter
        user_profile.save()
        return super().form_valid(form)


class ShelterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Shelter
    fields = [
        "name",
        "addressLine1",
        "addressLine2",
        "addressLine3",
        "city",
        "state",
        "zip",
        "phoneNumber",
        "webSite",
    ]

    def test_func(self):
        shelter = self.get_object()
        if self.request.user.profile.shelter == shelter:
            return True
        return False
