from django.urls import path
from .views import LoginView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('me/', UserDetailView.as_view(), name='me'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]