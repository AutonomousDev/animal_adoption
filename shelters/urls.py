from django.urls import path
from .views import (
    ShelterDetailView,
    ShelterListView,
    ShelterCreateView,
    ShelterUpdateView
)

urlpatterns = [
    path('', ShelterListView.as_view(), name='shelters-list'),
    path('<int:pk>/', ShelterDetailView.as_view(), name='shelters-detail'),
    path('new/', ShelterCreateView.as_view(), name='shelters-create'),
    path('characters/<int:pk>/update/', ShelterUpdateView.as_view(), name='shelter-update'),
]
