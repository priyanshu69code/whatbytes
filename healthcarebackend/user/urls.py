# users/urls.py
from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView


name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
