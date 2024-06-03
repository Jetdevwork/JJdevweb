from django.contrib import admin
from .models import History, Patient, Date

class HistoryInline(admin.TabularInline):
    model = History
    extra = 1
    
class DateInline(admin.TabularInline):
    model = Date
    extra = 1    
    
class PatientAdmin(admin.ModelAdmin):
    inlines = [HistoryInline, DateInline]
    list_display = (
        "identification_card", "name", "lastname", "age", "phone", "email",
    )

admin.site.register(Patient, PatientAdmin)
admin.site.register(History)
admin.site.register(Date)
