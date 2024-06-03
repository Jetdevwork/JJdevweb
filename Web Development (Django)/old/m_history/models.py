from django.db import models
from django.contrib.auth import get_user_model 
from django.urls import reverse
import uuid

class Patient(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    identification_card = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=320)

    def title(self):
        return f"{self.name}, {self.lastname}" 

    def __str__(self):
        return f"{self.name} {self.lastname}"           

    def get_absolute_url(self):
        return f'/patients/{self.id}/'

class History(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='history'
    )
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    time = models.DateTimeField(auto_now_add=True)
    reason_visit = models.TextField()
    records = models.TextField()
    current_diseases = models.TextField()
    physical_exam = models.TextField()
    diagnostic = models.TextField()
    therapeutic_plan = models.TextField()

    def title(self):
        return f"{self.patient.name}, {self.patient.lastname}"

    def __str__(self):
        return f"{self.patient.name} {self.patient.lastname} - {self.time}"

class Date(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='date'
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    description = models.TextField()
    appointment = models.DateTimeField()

    def title(self):
        return f"{self.patient.name}, {self.patient.lastname}"

    def __str__(self):
        return f"{self.patient.name} {self.patient.lastname} - {self.appointment}"


    
