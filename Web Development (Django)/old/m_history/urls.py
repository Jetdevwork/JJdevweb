from django.urls import path
from .views import PatientListView, PatientDetailView

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('<uuid:pk>', PatientDetailView.as_view(), name='patient_detail'), 
]

