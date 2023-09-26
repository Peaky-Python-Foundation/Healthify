from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


class Appointment(models.Model):
    speciality = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="doctor_appointed"
    )
    doctor = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="booked_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"By: {self.patient.first_name} for Dr. {self.doctor.first_name}"

    def get_absolute_url(self):
        return reverse("view_details", kwargs={"pk": self.pk})

    class Meta:
        ordering = ("-created_at",)