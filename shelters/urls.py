from django.urls import path
from .views import (
    ShelterDetailView,
    ShelterListView
)

urlpatterns = [
    path('', ShelterListView.as_view(), name='shelters-list'),
    path('<int:pk>/', ShelterDetailView.as_view(), name='job-post-detail'),
]
