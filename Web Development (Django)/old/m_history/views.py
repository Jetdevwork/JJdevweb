from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/patient_detail.html'  
