from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["doctor", "patient", "date", "time", "created_at"]
    search_fields = ("doctor", "patient")