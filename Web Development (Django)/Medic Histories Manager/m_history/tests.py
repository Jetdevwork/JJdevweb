from django.test import TestCase
from django.urls import reverse
from .models import Patient, History
import uuid

class PatientModelTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            identification_card="1234567890",
            name="John",
            lastname="Doe",
            age=30,
            phone="555-1234",
            email="john.doe@example.com"
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.name, "John")
        self.assertEqual(self.patient.lastname, "Doe")
        self.assertEqual(self.patient.age, 30)
        self.assertEqual(self.patient.phone, "555-1234")
        self.assertEqual(self.patient.email, "john.doe@example.com")

    def test_patient_string_representation(self):
        self.assertEqual(str(self.patient), "John Doe")

    def test_patient_title(self):
        self.assertEqual(self.patient.title(), "John, Doe") 

    def test_patient_get_absolute_url(self):
        self.assertEqual(self.patient.get_absolute_url(), f'/patients/{self.patient.id}/')


class HistoryModelTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            identification_card="1234567890",
            name="Jane",
            lastname="Doe",
            age=28,
            phone="555-5678",
            email="jane.doe@example.com"
        )
        self.history = History.objects.create(
            patient=self.patient,
            reason_visit="Routine Checkup",
            records="All records are up to date.",
            current_diseases="None",
            physical_exam="Normal",
            diagnostic="Healthy",
            therapeutic_plan="Continue regular checkups."
        )

    def test_history_creation(self):
        self.assertEqual(self.history.patient.name, "Jane")
        self.assertEqual(self.history.reason_visit, "Routine Checkup")
        self.assertEqual(self.history.records, "All records are up to date.")
        self.assertEqual(self.history.current_diseases, "None")
        self.assertEqual(self.history.physical_exam, "Normal")
        self.assertEqual(self.history.diagnostic, "Healthy")
        self.assertEqual(self.history.therapeutic_plan, "Continue regular checkups.")

    def test_history_string_representation(self):
        self.assertEqual(str(self.history), f"Jane Doe - {self.history.time}")

    def test_history_title(self):
        self.assertEqual(self.history.title(), "Jane, Doe")
