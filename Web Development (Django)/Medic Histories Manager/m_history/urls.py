from django.urls import path
from . import views
from .views import *

app_name = 'm_history'

urlpatterns = [
    # Patient URLs
    path('patients/list/', PatientListView.as_view(), name='patient_list'),
    path('patients/add/', PatientCreateView.as_view(), name='patient_add'),
    path('patients/<uuid:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patients/<uuid:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'), 
    path('patients/<uuid:pk>/update/', PatientUpdateView.as_view(), name='patient_update'),
    path('patients/<uuid:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'), 

    # History URLs
    path('patients/<uuid:pk>/history/add/', HistoryCreateView.as_view(), name='history_add'),
    path('patients/<uuid:pk>/history/edit/', HistoryUpdateView.as_view(), name='history_edit'),
    path('patients/<uuid:pk>/history/delete/', HistoryDeleteView.as_view(), name='history_delete'),

    # Date URLs
    path('patients/<uuid:pk>/date/add/', DateCreateView.as_view(), name='date_add'),
    path('patients/<uuid:pk>/date/edit/', DateUpdateView.as_view(), name='date_edit'),
    path('patients/<uuid:pk>/date/delete/', DateDeleteView.as_view(), name='date_delete'),
]
