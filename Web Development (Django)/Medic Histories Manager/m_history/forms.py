# forms.py
from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['identification_card', 'name', 'lastname',  'gender', 'address', 'age', 'phone', 'email']

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ['reason_visit', 'records', 'current_diseases', 'physical_exam', 'diagnostic', 'therapeutic_plan']

class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['description', 'appointment']
        widgets = {
            'appointment': forms.DateTimeInput(attrs={'id': 'id_appointment', 'class': 'form-control'})
        }