from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import AnimalFilterView

urlpatterns = [
    path('animals/', AnimalFilterView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # This is basically the logout:
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]