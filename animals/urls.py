from django.urls import path
from .views import (
    AnimalListView,
    AnimalDetailView
)

urlpatterns = [
    path('', AnimalListView.as_view(), name='animals-list'),
    path('<int:pk>/', AnimalDetailView.as_view(), name='animals-detail'),
]