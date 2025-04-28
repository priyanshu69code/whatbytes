# patients/models.py
from django.db import models
from django.conf import settings

class Patient(models.Model):
    # Gender Choice
    GENDER_CHOICES = [
        ("M","Male"),
        ("F","Female"),
        ("O","Other"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="O")
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
