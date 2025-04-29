# mappings/urls.py
from django.urls import path
from .views import (
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingDetailView,
    PatientDoctorMappingsByPatientView
)


name = 'mapping'
urlpatterns = [
    path('', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
    path('patient/<int:patient_id>/', PatientDoctorMappingsByPatientView.as_view(), name='mappings-by-patient'),
]
