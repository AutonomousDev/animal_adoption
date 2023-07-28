from django.db.models import F
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Animal, Shelter
from .filters import AnimalFilter
from django_filters.views import FilterView


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    fields = [
        "name",
        "species",
        "age",
        "breed",
        "availability",
        "disposition",
        "size",
        "image"
    ]

    def get_context_data(self, *args, **kwargs):
        context = super(AnimalCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Add a new animal to your shelter"
        return context

    def form_valid(self, form):
        form.instance.shelter = self.request.user.profile.shelter
        form.save()
        return super().form_valid(form)


class AnimalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Animal
    fields = [
        "name",
        "species",
        "age",
        "breed",
        "availability",
        "disposition",
        "size",
        "image"
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


class AnimalListView(ListView):
    model = Animal
    context_object_name = 'animals'


class AnimalFilterView(FilterView):
    model = Animal
    context_object_name = 'animals'
    filterset_class = AnimalFilter


class AnimalDetailView(DetailView):
    model = Animal
    context_object_name = 'animal'

    def get(self, request, *args, **kwargs):
        animal = self.get_object()
        Animal.objects.filter(pk=animal.pk).update(views=F('views') + 1)
        return super().get(request, *args, **kwargs)
