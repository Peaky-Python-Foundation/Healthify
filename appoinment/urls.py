from django.urls import path
from .views import (
    ListDoctors,
    BookAppointment,
    AllBookedAppointments,
    ViewAppointmentDetails,
)

urlpatterns = [
    path("doctors/", ListDoctors.as_view(), name="list_doctors"),
    path("doctors/<int:id>/book/", BookAppointment.as_view(), name="book_appointment"),
    path("all/", AllBookedAppointments.as_view(), name="list_appointments"),
    path("view/<int:pk>/", ViewAppointmentDetails.as_view(), name="view_details"),
]