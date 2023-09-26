from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home,
    DoctorSignUpView,
    PatientSignUpView,
    SignUpView,
)

urlpatterns = [
    path("",home,name='home'),
    path(
        "login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/doctor/", DoctorSignUpView.as_view(), name="signup_doctor"),
    path("signup/patient/", PatientSignUpView.as_view(), name="signup_patient"),

]
