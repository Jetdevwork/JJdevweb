from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

login_url = 'account_login'

# Patient Views
class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patient_list'

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patients/patient_detail.html'

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'patients/patient_confirm_delete.html'
    success_url = reverse_lazy('m_history:patient_list')


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Patient deleted successfully.")
        return super().delete(request, *args, **kwargs)

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_edit.html'
    success_url = reverse_lazy('m_history:patient_list')

    def form_valid(self, form):
        messages.success(self.request, "Patient details updated successfully.")
        return super().form_valid(form)
    
class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_add.html'
    success_url = reverse_lazy('m_history:patient_list')

    def form_valid(self, form):
        messages.success(self.request, "Patient added successfully.")
        return super().form_valid(form)


class HistoryCreateView(LoginRequiredMixin, CreateView):
    model = History
    form_class = HistoryForm
    template_name = 'histories/history_add.html'  
    success_url = reverse_lazy('m_history:patient_detail') 

    def form_valid(self, form):
        patient = get_object_or_404(Patient, pk=self.kwargs['pk'])
        form.instance.patient = patient
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('m_history:patient_detail', kwargs={'pk': self.kwargs['pk']})

class HistoryUpdateView(LoginRequiredMixin, UpdateView):
    model = History
    form_class = HistoryForm 
    template_name = 'histories/history_edit.html' 
    success_url = reverse_lazy('m_history:patient_detail')  

    def form_valid(self, form):
        messages.success(self.request, "Medical history updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        patient_uuid = self.object.patient.pk
        return reverse_lazy('m_history:patient_detail', kwargs={'pk': patient_uuid})
    
class HistoryDeleteView(LoginRequiredMixin, DeleteView):
    model = History
    template_name = 'histories/history_confirm_delete.html' 
    success_url = reverse_lazy('m_history:patient_list')

    def get_success_url(self):
        if self.object.patient:
            patient_uuid = self.object.patient.pk
            if patient_uuid:
                return reverse_lazy('m_history:patient_detail', kwargs={'pk': patient_uuid})
        return reverse_lazy('m_history:patient_list')  # Fallback URL

# Date Views
class DateCreateView(LoginRequiredMixin, CreateView):
    model = Date
    form_class = DateForm
    template_name = 'dates/date_add.html'  
    success_url = reverse_lazy('m_history:patient_detail') 

    def form_valid(self, form):
        patient = get_object_or_404(Patient, pk=self.kwargs['pk'])
        form.instance.patient = patient
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('m_history:patient_detail', kwargs={'pk': self.kwargs['pk']})

class DateUpdateView(LoginRequiredMixin, UpdateView):
    model = Date
    form_class = DateForm
    template_name = 'dates/date_edit.html'  
    success_url = reverse_lazy('m_history:patient_detail')   

    def form_valid(self, form):
        messages.success(self.request, "Dates updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        patient_uuid = self.object.patient.pk
        return reverse_lazy('m_history:patient_detail', kwargs={'pk': patient_uuid})
    
class DateDeleteView(LoginRequiredMixin, DeleteView):
    model = Date
    template_name = 'dates/date_confirm_delete.html'  
    success_url = reverse_lazy('m_history:patient_detail')   

    def get_success_url(self):
        if self.object.patient:
            patient_uuid = self.object.patient.pk
            if patient_uuid:
                return reverse_lazy('m_history:patient_detail', kwargs={'pk': patient_uuid})
        return reverse_lazy('m_history:patient_list')  # Fallback URL

