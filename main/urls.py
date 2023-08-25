from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("sign-in/", views.log_in, name="sign-in"),
    path("sign-out/", views.log_out, name="sign-out"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("registration/1", views.registration1, name="registration1"),
    path("registration/2", views.registration2, name="registration2"),
    path("registration/3", views.registration3, name="registration3"),
    path("form-submitted/", views.form_submitted, name="form-submitted"),
]
