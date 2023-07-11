from django.urls import path
from .views import (
    ShelterDetailView,
    ShelterListView,
    ShelterCreateView,
    ShelterUpdateView,
    ShelterDeleteView
)

urlpatterns = [
    path('', ShelterListView.as_view(), name='shelters-list'),
    path('<int:pk>/', ShelterDetailView.as_view(), name='shelters-detail'),
    path('new/', ShelterCreateView.as_view(), name='shelters-create'),
    path('<int:pk>/update/', ShelterUpdateView.as_view(), name='shelter-update'),
    path('<int:pk>/delete/', ShelterDeleteView.as_view(), name='shelter-delete'),
]
