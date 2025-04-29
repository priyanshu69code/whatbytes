# doctors/urls.py
from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDestroyView


name = 'doctor'
urlpatterns = [
    path('', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),
]
