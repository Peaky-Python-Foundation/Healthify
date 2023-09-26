from django.shortcuts import render, redirect
from .models import Appointment
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth import get_user_model
from django import forms


class ListDoctors(ListView):
    queryset = get_user_model().objects.filter(is_doctor=True)
    template_name = "appoinment/doctors.html"


class BookAppointment(CreateView):
    model = Appointment
    template_name = "appoinment/book_appointment_form.html"
    fields = ["speciality", "date", "time"]

    def get_form(self, form=None, **kwargs):
        new_form = super(BookAppointment, self).get_form()
        new_form.fields["date"].widget.input_type = "date"
        new_form.fields["time"].widget.input_type = "time"
        return new_form

    def form_valid(self, form):
        doctor_user = get_user_model()
        doctor = doctor_user.objects.get(id=self.kwargs["id"])
        appointment = form.save(commit=False)
        appointment.doctor = doctor
        appointment.patient = self.request.user
        appointment.save()
        return redirect(appointment.get_absolute_url())


class AllBookedAppointments(ListView):
    model = Appointment
    template_name = "appoinment/all_appointments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Appointment.objects.filter(
            doctor=self.request.user
        ) | Appointment.objects.filter(patient=self.request.user)
        return context


class ViewAppointmentDetails(DetailView):
    model = Appointment
    template_name = "appoinment/view_appointment_details.html"